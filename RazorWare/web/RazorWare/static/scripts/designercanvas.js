/**
 * Created by David on 7/18/2015.
 */

function DesignerCanvas (statusPane) {
    var $statusPane = new StatusPanel(statusPane);

    var $canvas = $("<div id='canvas'/>").droppable({
            accept: ".toolBoxItem",
            hoverClass: "drop_hover",
            over: function (event, ui) {
                console.log("tbItem detected: start movement tracking");
            },
            out: function (event, ui) {
                console.log("tbItem left canvas: stop movement tracking");
            },
            drop: function (event, ui) {
                $(this).append($(ui.draggable.clone()));
            }
        });

    this.control = $canvas;
    this.update = updatePosition;

    function updatePosition (element) {
        //console.log("[X: " + element.position.left + ", Y: " + element.position.top + "]");
        $statusPane.write("[X: " + element.position().left + ", Y: " + element.position().top + "]");
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