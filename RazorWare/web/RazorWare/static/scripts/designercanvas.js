/**
 * Created by David on 7/18/2015.
 */

function DesignerCanvas (statusPane, formManager) {
    var $statusPane = new StatusPanel(statusPane);
    var manager = new FormManager(this);

    var $canvas = $("<div id='canvas'/>").droppable({
            accept: ".toolBoxItem, .formItem",
            hoverClass: "drop_hover",
            over: function (event, ui) {
                console.log("tbItem detected: start movement tracking");
            },
            out: function (event, ui) {
                console.log("tbItem left canvas: stop movement tracking");
            },
            drop: function (event, ui) {
                if ($(ui.draggable).hasClass("toolBoxItem")) {
                    var $dropItem = $(ui.draggable.clone()).find(ui.draggable.attr("type"));
                    var currentPos = ui.helper.position();
                    currentPos.left = currentPos.left - $(this).position().left;
                    currentPos.top = currentPos.top - $(this).position().top;

                    $dropItem.css({
                        "left": currentPos.left,
                        "top": currentPos.top,
                        "position": "relative"
                    });
                    $dropItem.prop("title", "");
                    makeDraggable($dropItem);

                    $(this).append($dropItem);
                    updatePosition($dropItem);

                    manager.addControl($dropItem);
                }
            }
        });

    this.control = $canvas;
    this.update = updatePosition;

    manager.initialize();

    function updatePosition (element) {
        //console.log("[X: " + element.position.left + ", Y: " + element.position.top + "]");
        $statusPane.write("[X: " + element.position().left + ", Y: " + element.position().top + "]");
    }

    function makeDraggable(element) {
        //element.draggable({
        //    revert: "invalid"
        //});
        element.draggable();
        element.toggleClass("formItem");
    }
}

function StatusPanel(statusPane) {
    var $statusLabel = $("<label class='statusInfo'/>");
    initializeStatusPane();

    this.write = updatePanel;

    function initializeStatusPane() {
        statusPane.append($statusLabel);
    }

    function updatePanel(value) {
        $statusLabel.text(value);
    }
}