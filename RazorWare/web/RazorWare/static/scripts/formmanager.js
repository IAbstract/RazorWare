/**
 * Created by David on 7/20/2015.
 */

function FormManager(designer) {
    var $designer = designer;
    var controlIndexer = {};
    var controlCollection = [];
    var $currentControl = null;

    this.addControl = addFormControl;
    this.initialize = function () {
        $designer.control.on("click", clearControlSelection);
    };

    function addFormControl($control, type) {
        var id = getTypeId(type);
        $control.prop("id", id);
        $control.text("label" + id);

        controlCollection.push($control);
        $control.on("click", selectControl);
    }

    function selectControl(event) {
        if ($currentControl != null) {
            $currentControl.toggleClass("selectedFormItem");
        }

        $currentControl = $(event.currentTarget);
        $currentControl.toggleClass("selectedFormItem");
        event.stopPropagation();
        event.preventDefault();

        console.log("control selected: " + $currentControl.text());
    }

    function clearControlSelection() {
        if ($currentControl != null) {
            console.log("clear selected: " + $currentControl.text());
            $currentControl.toggleClass("selectedFormItem");
        }

        $currentControl = null;
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