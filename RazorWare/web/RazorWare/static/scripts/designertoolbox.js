/**
 * Created by David on 7/18/2015.
 */

function DesignerToolbox (toolsContent) {
    var $toolbox = buildToolbox();

    this.control = $toolbox;

    function buildToolbox() {
        var $toolsControl = $("<table/>");

        console.log("loading toolbox:");
        $.each(toolsContent, function (item) {
            console.log("\t<" + item + "/> \"" + toolsContent[item]['tooltip'] + "\" [" + toolsContent[item]['image'] + "]");
            var $row = $("<tr><td/></tr>");
            var $tool = $("<label/>");
            var $image = $("<img/>");
            $image.prop("title", toolsContent[item]['tooltip']);
            $image.prop("src", "/static/" + toolsContent[item]['image'])

            $tool.append($image);
            $row.find("td").append($tool);
            $toolsControl.append($row);
        });

        return $toolsControl;
    }
}