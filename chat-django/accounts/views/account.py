from accounts.models import Account
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView


class AccountView(TemplateView):
    template_name = 'accounts/pages/account.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        account_id = context.get('id')
        account = get_object_or_404(Account.objects.filter(
            pk=account_id
        ).select_related('author'), pk=account_id)

        return self.render_to_response({
            **context,
            'account': account,
        })
