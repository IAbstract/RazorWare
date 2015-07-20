/**
 * Created by David on 7/20/2015.
 */

function FormManager() {
    var $designer = null;
    var controlCollection = [];
    var $currentControl = null;

    this.setDesigner = function(designer) {
        $designer = designer;
    };

    this.addControl = addFormControl;


    function addFormControl(control) {
        controlCollection.push(control);
        control.on("click", selectControl);
    }

    function selectControl(e) {

        console.log("control selected")
    }
}