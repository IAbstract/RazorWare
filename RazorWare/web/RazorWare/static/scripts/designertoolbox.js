/**
 * Created by David on 7/18/2015.
 */

function DesignerToolbox (toolsContent, targetCanvas) {
    var toolBoxItems = [];
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
            var $tbItemContainer = $("<div class='toolBoxItem'/>");
            var $tbItem = $(toolsContent[item]['html']);
            $tbItem.css({
                "width": "100%",
                "height": "100%"
            });

            $tbItemContainer.append($tbItem);
            $tbItemContainer.attr("type", item);
            $tbItemContainer.prop("title", toolsContent[item]['tooltip']);
            
            toolBoxItems.push($tbItemContainer);

            $row.find("td").append($tbItemContainer);
            $toolBox.append($row);

            $tbItemContainer.draggable({
                helper: "clone",
                opacity: 0.5,
                containment: targetCanvas.prop("id")
            });
        });

        return $toolBox;
    }
}