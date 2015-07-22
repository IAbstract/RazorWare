/**
 * Created by David on 7/18/2015.
 */

var toolboxItems = {};

function DesignerToolbox (toolsContent, targetCanvas) {
    var updateDisplay = null;

    this.control = buildToolbox();
    this.setUpdate = function (updateDelegate) {
        updateDisplay = updateDelegate;
    };

    function buildToolbox() {
        var $toolBox = $("<table id='toolBox'/>");

        console.log("loading toolbox:");
        $.each(toolsContent, function (item) {
            console.log("\t<" + item + "/> \"" + toolsContent[item]['tooltip']);

            var $row = $("<tr><td/></tr>");

            var $tbItem = new ToolboxItem(toolsContent[item]['html'], item);
            $tbItem.setTarget(targetCanvas.prop("id"));
            $tbItem.setTitle(toolsContent[item]['tooltip']);
            
            toolboxItems[item] = ($tbItem);

            $row.find("td").append($tbItem.container);
            $toolBox.append($row);
        });

        return $toolBox;
    }
}

function ToolboxItem(tbItem, type) {
    var $tbItemContainer = $("<div class='toolBoxItem'/>");
    var $tbItem = $(tbItem);
    var dropTarget = null;

    this.container = $tbItemContainer;
    this.setTitle = function(title) {
        $tbItemContainer.prop("title", title);
    };
    this.setTarget = function(target) {
        dropTarget = target;
    };

    $tbItem.css({
        "width": "100%",
        "height": "100%"
    });
    $tbItemContainer.append($tbItem);
    $tbItemContainer.attr("type", type);

    $tbItemContainer.draggable({
        helper: "clone",
        opacity: 0.5,
        containment: dropTarget
    });
}