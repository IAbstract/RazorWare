/**
 * Created by David on 7/18/2015.
 */

function DesignerCanvas (statusPane, formManager) {
    var $statusPane = new StatusPanel(statusPane);
    var manager = new FormManager(this);

    var $canvas = $("<div id='canvas'/>").droppable({
            accept: ".toolBoxItem, .controlItem",
            hoverClass: "drop_hover",
            over: function (event, ui) {
                console.log("tbItem detected: start movement tracking");
            },
            out: function (event, ui) {
                console.log("tbItem left canvas: stop movement tracking");
            },
            drop: function (event, ui) {
                if ($(ui.draggable).hasClass("toolBoxItem")) {
                    var type = ui.draggable.attr("type");
                    var $control = new Control($(ui.draggable.clone()).find(type), $(this));
                    $control.position(ui.helper.position());
                    $control.makeDraggable();

                    $(this).append($control.base);
                    updatePosition($control.base);

                    manager.addControl($control, type);
                }
            }
        });

    this.control = $canvas;
    this.update = updatePosition;

    manager.initialize();
    this.propertyGrid = manager.propertyGrid;

    function updatePosition (element) {
        //console.log("[X: " + element.position.left + ", Y: " + element.position.top + "]");
        $statusPane.write("[X: " + element.position().left + ", Y: " + element.position().top + "]");
    }
}

function Control(tbItem, container) {
    var $control = $(tbItem);
    var $container = container;
    var position = {
        left: 0,
        top: 0
    };

    this.base = $control;
    this.container = $container;
    this.makeDraggable = function() {
        $control.draggable();
        $control.toggleClass("controlItem");
    };
    this.on = setEventHandler;
    this.position = function(currentPos) {
        position.left = currentPos.left - $container.position().left;
        position.top = currentPos.top - $container.position().top;
        
        $control.css({
            "left": position.left,
            "top": position.top,
            "position": "relative"
        });
    };
    this.setTitle = function(title) {
        $control.prop("title", title);
    };

    //  initialization
    $control.attr("title", "");

    function setEventHandler(event, delegate) {
        $control.on(event, this, delegate);
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