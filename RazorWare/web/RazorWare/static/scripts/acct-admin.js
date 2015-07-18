/**
 * Created by David Boarman on 3/3/2015.
 * (c) 2015, RazorWare, LLC
 */

var account;

var widgets = {
    ctrls: {}
};
var states = {
    start: "Fetching account information: ",
    ready: "Ready",
    save: "Setting up trial account ...",
    results: {
        true: "Account set-up complete",
        false: "There was a problem setting up the account"
    }
};

$(document).ready(function(){
    console.log("[script] acct-admin.js ready");

    widgets.ctrls = {
        $status: $("#action_status"),
        $acct_id: $("#acct_id")
    }
});

function fetch_account_data(acct_id){
    account = acct_id;
    widgets.ctrls.$status.html(states.start + account);
    $.getJSON("/razorcrm/query_account", {acct_id: account}, function(results){
        widgets.ctrls.$status.html(states.ready);
        widgets.ctrls.$acct_id.html("Account #: " + results.acct_id);
    });
}