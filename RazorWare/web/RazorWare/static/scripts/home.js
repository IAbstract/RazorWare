/**
 * Created by David Boarman on 2/24/2015.
 * (c) 2015, RazorWare, LLC
 */

var widgets = {
    trial_ctrls: {},
    company_info: {},
    contact_info: {}
};
var states = {
    start: "Click 'Create' button to create account for 30-day trial.",
    create: "<ul type='none'><li><b>Reset</b>: clear form</li><li><b>Cancel</b>: cancel new account</li></ul>",
    save: "Setting up trial account ...",
    results: {
        true: "Account set-up complete",
        false: "There was a problem setting up the account"
    }
};

var scripts_path;
var countries;
var addr_types_detail;

$(document).ready(function () {
    console.log("[script] home.js ready");

    widgets.trial_ctrls = {
        $status: $("#action_status"),
        $create: $("#create_trial"),
        $start: $("#start_trial"),
        $cancel: $(".cancel_trial"),
        $info: $(".trial_info")
    };

    widgets.company_info = {
        $name: $("#company_name"),
        $container: $("#tbl_company_address")
    };

    widgets.contact_info = {
        $fname: $("#contact_fname"),
        $mname: $("#contact_mname"),
        $sname: $("#contact_lname"),
        $phone: $("#contact_phone"),
        $email: $("#contact_email"),
        $container: $("#tbl_contact_address")
    };

    widgets.trial_ctrls.$status.html(states.start);
    widgets["$contact_addr_same"] = $("#contact_addr_same");
    widgets["$contact_addr_info"] = $("#contact_addr_info");

    setControlBindings();
    setControlStates();
});

function addAddrTable(owner, table_id) {
    AddressTable(owner, table_id);
    owner.$container.append(owner.$table);

    //   bindings
    setAddrStateBindings(owner);
}

function setAddrStateBindings(owner) {
    owner.$loc_type.bind("change", function () {
        owner.$loc_info.html(addr_types_detail[owner.$loc_type.val()]);
    });
    $.each(addr_types_detail, function (item) {
        owner.$loc_type.append(new Option(item, item));
    });
    owner.$loc_type.val("Business.Primary");
    owner.$loc_type.trigger("change");

    owner.$search_postal.bind("click", function () {
        queryLocaleByPostCode(owner);
    });
}

function setControlStates() {
    widgets.trial_ctrls.$info.hide();
    widgets.$contact_addr_info.hide();
}

function setControlBindings() {
    widgets.trial_ctrls.$create.bind("click", createAccount);
    widgets.trial_ctrls.$start.bind("click", startTrial);
    widgets.trial_ctrls.$cancel.bind("click", cancelAccount);

    widgets.$contact_addr_same.bind("change", setAddrDisplay);
}

function queryLocaleByPostCode(target) {
    var post_code = target.$loc_postal.val();
    $.getJSON("/razorcrm/query_locale", {post_code: post_code}, function (results) {
        console.log("[APP] query locale for: " + post_code + " [returned: " + results.success + "]");

        if (results.success) {
            var locale = results.location["city"] + ", " +
                results.location["state_region"] + "  " +
                results.location["post_code"] + " [" +
                results.location["country"] + "]";
            console.log("[APP] locale: " + locale);
            displayLocaleInfo(target, results.location);
        } else {
            console.log("[APP] query failed!");
        }
    });
}

function displayLocaleInfo(target, location) {
    target.$loc_city.val(location["city"]);
    target.$loc_state.val(location["state_region"]);
    target.$loc_country.html(countries[location["country"]]);
    target.$loc_country.attr("code", location["country"]);
}

function setAddrDisplay() {
    if (widgets.$contact_addr_same.prop("checked")) {
        widgets.$contact_addr_info.hide();
        if (widgets.contact_info.hasOwnProperty("$table")) {
            var $table = widgets.contact_info.$table;
            $table.remove();
        }
    } else {
        addAddrTable(widgets.contact_info, "contact_address");
        widgets.$contact_addr_info.show();
    }
}

function createAccount() {
    var action = widgets.trial_ctrls.$create.val();

    if (action == "Create") {
        widgets.trial_ctrls.$create.val("Reset");
        widgets.trial_ctrls.$status.html(states.create);
        addAddrTable(widgets.company_info, "company_address");
        widgets.trial_ctrls.$info.show();
    } else if (action == "Reset") {
        //  clear/reset info
        widgets.trial_ctrls.$cancel.trigger("click");
        widgets.trial_ctrls.$create.trigger("click");
        resetFields(widgets.company_info);
        resetFields(widgets.contact_info);
    }
}

function resetFields(info_set) {
    $.each(info_set, function (i, e) {
        if (e.attr("type") === "text") {
            e.val("");
        }
    });
}

function cancelAccount() {
    //  clear/reset info ???
    if (widgets.company_info.hasOwnProperty("$table")) {
        var $table = widgets.company_info.$table;
        $table.remove();
    }
    widgets.trial_ctrls.$status.html(states.start);
    widgets.$contact_addr_same.prop("checked", true);
    widgets.$contact_addr_same.trigger("change");
    widgets.trial_ctrls.$create.val("Create");
    widgets.trial_ctrls.$info.hide();
}

function startTrial() {
    var company = widgets.company_info;
    var contact = widgets.contact_info;

    var trial_info = {
        company: {
            name: company.$name.val(),
            address: {
                line_1: company.$addr_line_1.val(),
                line_2: company.$addr_line_2.val(),
                city: company.$loc_city.val(),
                state: company.$loc_state.val(),
                postal: company.$loc_postal.val(),
                country: company.$loc_country.attr("code")
            }
        }
    };
    trial_info["contact"] = {
        fname: contact.$fname.val(),
        mname: contact.$mname.val(),
        sname: contact.$sname.val(),
        phone: contact.$phone.val(),
        email: contact.$email.val(),
        //  if contact addr same as company
        address: contact.hasOwnProperty("$addr_line1") ?
        {
            line_1: contact.$addr_line_1.val(),
            line_2: contact.$addr_line_2.val(),
            city: contact.$loc_city.val(),
            state: contact.$loc_state.val(),
            postal: contact.$loc_postal.val(),
            country: contact.$loc_country.attr("code")
        } : trial_info.company.address
    };

    var data = {
        trial_info: JSON.stringify(trial_info) //,
        //csrfmiddlewaretoken: csrf_token
    };

    widgets.trial_ctrls.$status.html(states.save);
    $.getJSON("/razorcrm/start_trial", data, function (results) {
        widgets.trial_ctrls.$status.html(states.results[results.success]);
        if(results.success){
            var acct_num = results.company["account"];
            console.log("Company Account created: " + acct_num);
            window.location = "/razorcrm/" + acct_num + "/admin"
        } else {
            alert(results.err_msg);
        }
    });
}

function cacheScriptsPath(static_scripts_path) {
    console.log("[script] set scripts path: " + static_scripts_path);
    scripts_path = static_scripts_path;

    loadScript("addresstable.js", function () {
        console.log("[script] addresstable.js ready");
    });
}

function cacheCountries(country_list) {
    countries = country_list;
    var isCached = countries ? true : false;
    console.log("[RzApp] country list cached: " + isCached);
    console.log("[RzApp] US: " + countries.US);
}

function cacheAddrTypes(addr_types_list) {
    addr_types_detail = addr_types_list;
}

function loadScript(source, callback) {
    // Adding the script tag to the head as suggested before
    var source_path = scripts_path + "/" + source;
    console.log("[script] loading: " + source_path);

    var head = document.getElementsByTagName('head')[0];
    var script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = source_path;

    // Then bind the event to the callback function.
    // There are several events for cross browser compatibility.
    script.onreadystatechange = callback;
    script.onload = callback;

    // Fire the loading
    head.appendChild(script);
}
