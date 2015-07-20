/**
 * Created by David on 7/20/2015.
 */

function FormManager(designer) {
    var $designer = designer;
    var controlCollection = [];
    var $currentControl = null;

    this.addControl = addFormControl;
    this.initialize = function () {
        $designer.control.on("click", clearControlSelection);
    };

    function addFormControl(control) {
        controlCollection.push(control);
        control.on("click", selectControl);
    }

    function selectControl(e) {
        if ($currentControl != null) {
            $currentControl.toggleClass("selectedFormItem");
        }

        $currentControl = $(e.currentTarget);
        $currentControl.toggleClass("selectedFormItem");

        console.log("control selected: ");
    }

    function clearControlSelection() {
        if ($currentControl != null) {
            $currentControl.toggleClass("selectedFormItem");
        }
    }
}