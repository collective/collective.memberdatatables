jq(document).ready(function() {
  datatableconfig = {
      "iDisplayLength": -1,
      "aLengthMenu": [[100, 200, 500, -1],[100, 200, 500, "All"]]};
  jq('body.template-member_search_results .listing').dataTable(datatableconfig);
  jq('body.template-prefs_group_members .listing').dataTable(datatableconfig);
  jq('body.template-prefs_groups_overview .listing').dataTable(datatableconfig);
  jq('body.template-prefs_users_overview .listing').dataTable(datatableconfig);
  jq('body.template-prefs_users_roles .listing').dataTable(datatableconfig);
  jq('body.template- #user-group-sharing').dataTable(datatableconfig);
});