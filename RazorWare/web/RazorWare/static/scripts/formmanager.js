/**
 * Created by David on 7/20/2015.
 */

function FormManager(designer) {
    var $designer = designer;
    var controlIndexer = {};
    var controlCollection = [];
    var $currentControl = null;
    var $propertyBag = new PropertyBag();

    this.addControl = addFormControl;
    this.initialize = function () {
        $designer.control.on("click", clearControlSelection);
    };
    this.propertyBag = $propertyBag;

    function addFormControl($control, type) {
        var id = getTypeId(type);
        $control.prop("id", id);
        //  how to distinguish display values between controls?
        //  text is specific to label!!
        $control.text(type + "." + id);

        controlCollection.push($control);
        $control.on("click", selectControl);
    }

    function selectControl(event) {
        if ($currentControl != null) {
            $currentControl.toggleClass("selectedFormItem");
        }

        $currentControl = $(event.currentTarget);
        $currentControl.toggleClass("selectedFormItem");
        $propertyBag.displayProperties($currentControl);

        console.log("control selected: " + $currentControl.text());
        //  prevents event propagation (bubbling to parent container)
        return false;
    }

    function clearControlSelection() {
        if ($currentControl != null) {
            console.log("clear selected: " + $currentControl.text());
            $currentControl.toggleClass("selectedFormItem");
        }

        $currentControl = null;
        $propertyBag.clearProperties();
    }

    function getTypeId(type) {
        if (controlIndexer.hasOwnProperty(type)) {
            controlIndexer[type] += 1;
        } else {
            controlIndexer[type] = 0;
        }

        return controlIndexer[type];
    }
}

function PropertyBag() {
    var controlProperties = {};
    var $container = null;
    var $current = null;

    this.setContainer = function ($propertyContainer) {
        $container = $propertyContainer;
    };
    this.displayProperties = renderPropertiesDisplay;
    this.clearProperties = function(){
        if ($current != null) {
            $current.remove();
        }
    };

    function renderPropertiesDisplay($control) {
        var id = $control.prop("id");
        if (!controlProperties.hasOwnProperty(id)) {
            controlProperties[id] = buildPropertiesDisplay($control);
        }

        if ($current != null) {
            $current.remove();
        }
        $current = controlProperties[id];
        $container.append($current);
    }

    function buildPropertiesDisplay($control) {
        var $propBag = $("<table style='width: 100%; height: 100%;'/>");

        $.each($control[0].attributes, function(i, attr){
            var $row = new PropertyRow();

            var $name = $row.find(".propertyName");
            $name.text(attr.name);

            var $value = $row.find(".propertyField");
            $value.val(attr.value);

            $propBag.append($row);
        });

        return $propBag;
    }

    function PropertyRow() {
        return $("<tr><td class='propertyName'/><td><input type='text' class='propertyField'/></td></tr>");
    }
}