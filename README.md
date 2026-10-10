# Scripts de Automação

Coleção de scripts em Python para automação e organização de tarefas no sistema operacional.

---

## 📁 Estrutura do Projeto

```text
Scripts/
├── windows/
│   └── download.py       # Script de organização da pasta Downloads
└── README.md             # Documentação do projeto
```

---

## 🚀 Scripts Disponíveis

### 1. Organizador de Downloads (`windows/download.py`)

O script `download.py` é responsável por varrer o diretório de downloads do usuário (`Path.home() / "Downloads"`) e distribuir automaticamente os arquivos baixados para as pastas nativas padrão do sistema (compatível com nomes em Português e Inglês no Windows).

#### ✨ Principais Recursos

- **Diretórios Nativos do Sistema:** Mapeia e move os arquivos diretamente para as pastas de usuário correspondentes (`Imagens` / `Pictures`, `Documentos` / `Documents`, `Músicas` / `Music`, `Vídeos` / `Videos`).
- **Prevenção de Sobrescrita:** Se já existir um arquivo de mesmo nome na pasta de destino, ele é renomeado automaticamente com sufixo numérico incremental (ex.: `documento (1).pdf`).
- **Segurança Operacional:** Ignora subpastas para não desestruturar diretórios já criados e mantém arquivos executáveis/instaladores (`.exe`, `.msi`) na pasta Downloads.
- **Flexibilidade:** Permite execução direta na pasta padrão ou utilização como função recebendo um caminho customizado.

#### 📂 Mapeamento de Extensões

| Categoria | Destino Padrão | Extensões Suportadas |
| :--- | :--- | :--- |
| **Imagens** | `Pictures` / `Imagens` | `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.svg`, `.bmp`, `.ico`, `.tiff` |
| **Documentos** | `Documents` / `Documentos` | `.pdf`, `.docx`, `.doc`, `.txt`, `.pptx`, `.ppt`, `.odt`, `.rtf` |
| **Planilhas** | `Documents` / `Documentos` | `.xlsx`, `.xls`, `.csv`, `.ods` |
| **Compactados**| `Documents` / `Documentos` | `.zip`, `.rar`, `.7z`, `.tar`, `.gz` |
| **Áudio** | `Music` / `Músicas` | `.mp3`, `.wav`, `.aac`, `.flac`, `.ogg`, `.wma`, `.m4a` |
| **Vídeo** | `Videos` / `Vídeos` | `.mp4`, `.mkv`, `.avi`, `.mov`, `.wmv`, `.flv`, `.webm` |
| **Executáveis** | `Downloads` (permanece) | `.exe`, `.msi` |

---

## 🛠️ Como Usar

### Pré-requisitos

- Python 3.9 ou superior (utiliza apenas módulos da biblioteca padrão do Python, como `pathlib`, `shutil` e `typing`).

### Execução via Terminal

Para organizar a pasta de Downloads padrão do seu usuário:

```powershell
python windows/download.py
```

### Uso como Módulo Python

Você também pode importar a função `clean_download_dir` em outros scripts e passar um caminho personalizado:

```python
from pathlib import Path
from windows.download import clean_download_dir

# Executa na pasta padrão de Downloads do usuário
clean_download_dir()

# Ou executa em um diretório específico
clean_download_dir(Path("C:/meu_diretorio_personalizado"))
```
