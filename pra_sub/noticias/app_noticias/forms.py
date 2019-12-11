from django import forms


class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=128, min_length=4)
    email = forms.EmailField(required=False)
    mensagem = forms.CharField(widget=forms.Textarea)
    def clean(self):
        dados = super().clean()
        email = dados.get('email', None)
        mensagem = dados.get('mensagem')
        if '@hotmail.com' in email:
            self.add_error('email', 'Provedor nao suportado (@hotmail.com ou @yahoo.com)')
        palavras = ['problema', 'merda', 'defeito', 'erro']
        for palavra in palavras:
            if palavra in mensagem.lower():
                self.add_error('mensagem', 'Mensagem contem palavra nao permitida')
        return dados