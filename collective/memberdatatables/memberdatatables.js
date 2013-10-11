$(document).ready(function() {
    datatableconfig = {
            "iDisplayLength": -1,
            "aLengthMenu": [[100, 200, 500, -1],[100, 200, 500, "All"]],
            "oLanguage": {
                "sUrl": "@@collective.js.datatables.translation"
            }
    };
    $('body.template-member_search_results .listing').dataTable(datatableconfig);
    $('body.template-usergroup-groupprefs .listing').dataTable(datatableconfig);
    $('body.template-usergroup-userprefs .listing').dataTable(datatableconfig);
    $('body.template-usergroup-groupmembership .listing').dataTable(datatableconfig);
});