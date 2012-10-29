from zope import interface
from plone.app.workflow.browser import sharing
from Acquisition import aq_inner, aq_parent, aq_base

from zope.component import getMultiAdapter
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class SharingView(sharing.SharingView):
    """Override sharing view to use datatables"""

    template = ViewPageTemplateFile('sharing.pt')

    def _principal_search_results(self,
                                  search_for_principal,
                                  get_principal_by_id,
                                  get_principal_title,
                                  principal_type,
                                  id_key):

        context = aq_inner(self.context)
        
        existing_principals = set([p['id'] for p in self.existing_role_settings()
                                if p['type'] == principal_type])
        empty_roles = dict([(r['id'], False) for r in self.roles()])
        info = []

        hunter = getMultiAdapter((context, self.request), name='pas_search')

        if principal_type == 'user':
            all = hunter.searchUsersByRequest(self.request, sort_by='fullname')
        else:
            all = hunter.searchGroupsByRequest(self.request)

        for principal_info in all:
            principal_id = principal_info[id_key]
            if principal_id not in existing_principals:
                principal = get_principal_by_id(principal_id)
                roles = empty_roles.copy()
                if principal is None:
                    continue

                for r in principal.getRoles():
                    if r in roles:
                        roles[r] = 'global'
                info.append(dict(id    = principal_id,
                                 title = get_principal_title(principal,
                                                             principal_id),
                                 type  = principal_type,
                                 roles = roles))
        return info