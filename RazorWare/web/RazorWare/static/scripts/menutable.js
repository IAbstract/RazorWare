/**
 * Created by David on 6/25/2015.
 */

$(document).ready(function(){
    console.log("[script] menutable.js loaded");
});

function Menu(optionsObject, popupWindow) {
    var menus = {};
    var popups = {};
    var menuTips = {};
    var $menu = menu();
    var $popupWindow = popupWindow;

    this.control = $menu;
    this.setEvent = setEventDelegate;
    this.addPopupMenu = setPopupOptions;
    this.onAppear = onMenuBarAppear;

    function menu() {
        if (optionsObject.hasOwnProperty("tips")) {
            menuTips = optionsObject.tips;
        }

        $menu = $("<div id='menu'></div>");
        var $lastOpt = null;
        var leftPosition = 0;

        $.each(optionsObject['opts_order'], function (idx, imgInfo) {
            imgInfo = imgInfo.split(":");
            var option = imgInfo[0];
            var width = imgInfo[1];

            if (option.substring(0, 5) === "space") {
                var $spacer = $("<img style='height: 25px;width: " + width + "px;' src='/static/images/blank_spacer.png'/>");

                if ($lastOpt == null) {
                    $menu.prepend($spacer);
                } else {
                    $lastOpt.after($spacer);
                }

                $lastOpt = $spacer;

                //  should continue loop
                return true;
            }


            var $image = $("<img class='' id='" + option + "' src='/static/" + optionsObject[option] + "'/>");
            $image.css({width: width});

            menus[option] = $image;
            if (menuTips.hasOwnProperty(option)) {
                $image.prop("title", menuTips[option]);
            }

            if (option === "login") {
                //  login always at the end (right-justified)

                $menu.append($image);
            } else {
                if ($lastOpt == null) {
                    $menu.prepend($image);
                } else {
                    $lastOpt.after($image);
                }

                $lastOpt = $image;
            }

            leftPosition += width;
        });

        var spacerWidth = 75;
        //  insert blank cell to take up rest of space
        if ($lastOpt != null) {
            var $dynamicSpacer = $("<img id='spacer' style='height: 25px;width: " + spacerWidth + "px;' src='/static/images/blank_spacer.png'/>");

            $lastOpt.after($dynamicSpacer);
        }

        return $menu;
    }

    function onMenuBarAppear(e) {
        adjustMenuSpacer(e);
        assignSubMenuEvents(e);
    }

    function adjustMenuSpacer(e) {
        var imagesWidth = 0;
        var $imgList = $menu.find("img");
        var $spacer = null;

        $.each($imgList, function (idx, image) {
            //  tabulate image widths
            var $image = $(image);

            if ($image.prop("id") === "spacer") {
                $spacer = $image;
            } else {
                imagesWidth += $image.width();
            }
        });

        if ($spacer !== null) {
            var spacerWidth = $menu.width() - imagesWidth;
            $spacer.css({width: spacerWidth});
        }
    }

    function assignSubMenuEvents(e) {
        if (!optionsObject.hasOwnProperty('sub_opts')) {
            return;
        }

        console.log("[script::Menu] assign sub-menu events");
        var subOpts = optionsObject.sub_opts;

        $.each(subOpts, function (menu) {
            $.each(subOpts[menu], function (idx, subOpt) {
                if (!menus.hasOwnProperty(subOpt)) {
                    return true;    //  continue to next
                }
                if (subOpt === "separator") {
                    return true;
                }

                console.log("[script::Menu::" + menu + "] " + subOpt);
                setEventDelegate(subOpt, "mouseenter", toggleSubMenu, {subOpt: subOpt});
                setEventDelegate(subOpt, "mouseleave", toggleSubMenu, {subOpt: subOpt});
            });
        });
    }

    function toggleSubMenu(e) {
        //console.log(e.type + " option: " + e.data.subOpt);
        var $subOpt = menus[e.data.subOpt];
        $subOpt.toggleClass("popup_highlight");
    }

    function setEventDelegate(optName, event, eventDelegate, data) {
        var $control = $("#" + menus[optName].prop("id"));
        if (data == null) {
            $control.on(event, eventDelegate);
        } else {
            $control.on(event, data, eventDelegate);
        }
    }

    function setPopupOptions(menu, options) {
        var $popup = $("<div class='popup' id='" + menu + "popup'></div");

        //var $optList = $("<table></table>");
        //$popup.append($optList);

        $.each(options, function (idx, option) {
            var $option = null;
            if (option !== "separator") {
                $option = $("<label>" + option + "</label>");
            } else {
                $option = $("<hr>");
            }
            $option = $("<div class='popup_option' id='" + menu + option + "'/>").append($option);
            $popup.append($option);

            menus[option] = $option;
        });


        setPopupLocation($popup, menu);
        var top = $popup.css("top");
        var left = $popup.css("left");
        console.log("[script::Menu] location of " + menu + " popup [" + top + "," + left + "]");

        //  cache popup reference
        popups[menu] = $popup;

        //  append popup to document body
        $popupWindow.append($popup);
        setEventDelegate(menu, "mousemove", function (e) {
            if (popups[menu].attr("visible") == "false") {
                showPopup(e);
            }
        }, {menu: menu});
        setEventDelegate(menu, "mouseover", showPopup, {menu: menu});
        setEventDelegate(menu, "mouseleave", hidePopup, {menu: menu});
        setEventDelegate(menu, "click", function (e) {
            $popup.hide();
        });

        //  hide popup
        $popup.hide();
        $popup.attr("visible", false);

        //  popup mouse enter
        $popup.on("mouseenter", function (e) {
            console.log("[" + $popup.prop("id") + "::live] " + $popup.is(":hover"));
        });
        $popup.on("mouseleave", function (e) {
            hidePopup({data: {menu: menu}});

            console.log("[" + $popup.prop("id") + "::live] " + $popup.is(":hover"));
        });
        $popup.on("click", function (e) {
            $popup.hide();
        });
    }

    function showPopup(e) {
        var menu = e.data.menu;
        var $popup = popups[menu];

        console.log("[script::Menu] show " + menu + "#" + $popup.prop("id") +
            " @[" + $popup.css("top") + "," + $popup.css("left") + "]");
        $popup.slideDown();
        $popup.attr("visible", true);

        var location = $popup.position();
        console.log("[script::Menu] " + menu + "#" + $popup.prop("id") +
            " @[" + location.top + "," + location.left + "]");
    }

    function hidePopup(e) {
        var checkTimer = null;
        var menu = e.data.menu;
        var $popup = popups[menu];

        var do_hide = !$popup.is(":hover");
        console.log("[" + $popup.prop("id") + "::live] do hide: " + do_hide);
        checkTimer = setTimeout(function () {
            if (do_hide) {
                console.log("[script::Menu] hide " + menu + "#" + $popup.prop("id"));
                $popup.slideUp();
                $popup.attr("visible", false);
                clearInterval(checkTimer);
            }
        }, 25);
    }

    function setPopupLocation($popup, menu) {
        var $image = menus[menu];

        var location = $image.position();
        var popupTop = location.top + $image.height();
        var popupLeft = location.left;

        console.log("[script::Menu] set " + menu + " popup location => [" + popupTop + "," + popupLeft + "]");
        $popup.css({top:popupTop, left:popupLeft});
    }
}