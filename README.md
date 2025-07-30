# Sistema de Chamados

Sistema web para abertura e gerenciamento de chamados com funcionalidades de login persistente, upload de imagens e integração com Airtable.

## 🚀 Funcionalidades

- ✅ **Login Persistente**: Login mantido durante a sessão do navegador
- ✅ **Interface Moderna**: Design responsivo com logo personalizada
- ✅ **Upload de Imagens**: Sistema de anexos com drag-and-drop
- ✅ **Integração Airtable**: Dados salvos automaticamente
- ✅ **Visualização de Chamados**: Painel administrativo completo

## 🛠️ Tecnologias

- **Frontend**: HTML5, CSS3, JavaScript, Tailwind CSS
- **Backend**: Python Flask
- **Banco de Dados**: SQLite + Airtable
- **Deploy**: Fly.io
- **Controle de Versão**: Git/GitHub

## 📋 Pré-requisitos

- Python 3.11+
- Flask
- Flask-CORS
- Conta Airtable (configurada)

## 🔧 Instalação Local

1. Clone o repositório:
```bash
git clone https://github.com/SEU_USUARIO/sistema-chamados.git
cd sistema-chamados
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute a aplicação:
```bash
python src/main.py
```

5. Acesse: http://localhost:8080

## 🔐 Credenciais

- **Usuário**: admin2
- **Senha**: admin2

## 🚀 Deploy no Fly.io

1. Instale o Flyctl:
```bash
# Siga as instruções em: https://fly.io/docs/hands-on/install-flyctl/
```

2. Faça login:
```bash
flyctl auth login
```

3. Crie a aplicação:
```bash
flyctl apps create sistema-chamados-SEU-NOME
```

4. Faça o deploy:
```bash
flyctl deploy
```

## 📁 Estrutura do Projeto

```
sistema-chamados/
├── src/
│   ├── static/           # Frontend (HTML, CSS, JS)
│   ├── routes/           # Rotas Flask
│   ├── models/           # Modelos de dados
│   ├── database/         # Banco SQLite
│   └── main.py          # Aplicação principal
├── Dockerfile           # Container Docker
├── fly.toml            # Configuração Fly.io
├── requirements.txt    # Dependências Python
└── README.md          # Este arquivo
```

## 🔄 Atualizações

Para atualizar o sistema em produção:

```bash
git add .
git commit -m "Descrição das mudanças"
git push origin main
flyctl deploy
```

## 📞 Suporte

Para dúvidas ou problemas, abra uma issue no repositório GitHub.

---

**Desenvolvido com ❤️ usando Flask e Fly.io**

