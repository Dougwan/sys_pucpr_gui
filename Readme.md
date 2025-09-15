
## Requisitos

- Python 3.9+ (recomendado)

## Passo a passo para rodar o projeto

1. **Criar e ativar o ambiente virtual**:
   ```bash
   python -m venv venv
   ```

   - **Linux/MacOS**:
     ```bash
     source venv/bin/activate
     ```

   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```

2. **Instalar as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar variáveis de ambiente**:
   Copiar o arquivo de exemplo e ajustar os valores conforme necessário:
   ```bash
   cp .env.example .env
   ```

   *(No Windows PowerShell, use `copy .env.example .env`)*

4. **Executar a aplicação**:
   ```bash
   python main.py
   ```
