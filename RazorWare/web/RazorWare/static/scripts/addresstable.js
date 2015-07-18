/**
 * Created by David Boarman on 2/24/2015.
 * (c) 2015, RazorWare, LLC
 */

$(document).ready(function(){
    console.log("[script] addresstable.js loaded");

});

function AddressTable(owner, table_id){
    owner["$table"] = $(writeTable(table_id));
    owner["$addr_line_1"] = $("#address_line1", owner.$table);
    owner["$addr_line_2"] = $("#address_line2", owner.$table);
    owner["$loc_postal"] = $("#loc_zip", owner.$table);
    owner["$loc_city"] = $("#loc_city", owner.$table);
    owner["$loc_state"] = $("#loc_state", owner.$table);
    owner["$loc_country"] = $("#loc_country", owner.$table);
    owner["$loc_type"] = $("#loc_type", owner.$table);
    owner["$loc_info"] = $("#loc_type_info", owner.$table);
    owner["$search_postal"] = $("#search_zip", owner.$table);

    function writeTable(table_id){
        return "<div>" +
            "<table id='" + table_id + "' class='inner_content'>" +
                "<!-- location type info -->" +
                "<tr>" +
                    "<td colspan='2' style='height: auto;'><label id='loc_type_info' class='small_info'></label></td>" +
                "</tr>" +
                "<!-- street address -->" +
                "<tr>" +
                    "<td style='width: auto;'><label for='address_line1'>Street</label></td>" +
                    "<td style='width: 100%;'>" +
                        "<input id='address_line1' type='text' style='width: 75%;'/>" +
                    "</td>" +
                "<tr>" +
                "<tr>" +
                    "<td></td>" +
                    "<td style='width: 100%;'>" +
                        "<input id='address_line2' type='text' style='width: 75%;'/>" +
                    "</td>" +
                "</tr>" +
                "<!-- city, state/region, zip -->" +
                "<tr>" +
                    "<td colspan='2'>" +
                        "<table width='100%'>" +
                            "<tr>" +
                                "<td><label for='loc_city'>City</label></td>" +
                                "<td style='width: 55%;'><input id='loc_city' type='text' style='width: 100% !important;'/></td>" +
                                "<td><label for='loc_state'>State/Region</label></td>" +
                                "<td style='width: auto;'><input id='loc_state' type='text' style='width: 25px !important;'/></td>" +
                                "<td><label for='loc_zip' >Zip/Post</label></td>" +
                                "<td style='width: auto;'><input id='loc_zip' type='text' style='width: 75px !important;'/></td>" +
                                "<td><input id='search_zip' type='button'/></td>" +
                                "<td style='width: 100%;'></td>" +
                            "</tr>" +
                        "</table>" +
                    "</td>" +
                "</tr>" +
                "<!-- country, location type select -->" +
                "<tr>" +
                    "<td colspan='2'>" +
                        "<table width='100%'>" +
                            "<tr>" +
                                "<td>Country</td>" +
                                "<td style='width: 50%;'><label id='loc_country'></label></td>" +
                                "<td style='width: 50%;'><label for='loc_type'>Address Type</label>" +
                                    "<select id='loc_type'></select>" +
                                "</td>" +
                            "</tr>" +
                        "</table>" +
                    "</td>" +
                "</tr>" +
            "</table></div>";
    }

    //return $table;
}