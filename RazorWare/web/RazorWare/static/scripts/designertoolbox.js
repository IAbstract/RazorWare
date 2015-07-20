/**
 * Created by David on 7/18/2015.
 */

function DesignerToolbox (toolsContent) {
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
            var $tbItem = $(toolsContent[item]['html']);
            $tbItem.prop("title", toolsContent[item]['tooltip']);
            $tbItem.toggleClass("toolBoxItem");
            
            toolBoxItems.push($tbItem);

            $row.find("td").append($tbItem);
            $toolBox.append($row);

            $tbItem.draggable({
                helper: "clone",
                opacity: 0.5,
                drag: function (event, ui) {
                    //console.log("dragging " + ui.helper.attr("type"));
                    if (updateDisplay != null) {
                        updateDisplay($(ui.helper));
                    }
                }
            });
        });

        return $toolBox;
    }
}