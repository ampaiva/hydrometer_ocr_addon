# Gerando ícones para o Addon Hydrometer OCR

Este guia explica como gerar os arquivos `icon.png` e `logo.png` para o addon.

## Pré-requisitos

- Python 3.6+
- PIL/Pillow library

## Instalação das dependências

```bash
pip install Pillow
```

## Gerando os ícones

Para gerar os ícones, execute o script `create_icons.py` a partir do diretório `hydrometer_ocr`:

```bash
cd hydrometer_ocr
python3 create_icons.py
```

Este comando irá gerar dois arquivos PNG na mesma pasta:

### icon.png
- **Tamanho**: 256x256 pixels
- **Cor**: Azul (Steel Blue com detalhes em Turquesa)
- **Design**: Ícone de hidrômetro digital com círculos representando números
- **Uso**: Usar como ícone principal do addon no Home Assistant

### logo.png
- **Tamanho**: 512x128 pixels
- **Cor**: Fundo azul escuro com ícone turquesa
- **Design**: Logotipo horizontal com ícone de hidrômetro + texto "Hydrometer OCR"
- **Uso**: Usar para header, documentação ou apresentação do addon

## Cores utilizadas

- **Steel Blue**: RGB(25, 130, 180) - Cor de fundo principal
- **Medium Turquoise**: RGB(72, 209, 204) - Elementos e detalhes
- **Dark Blue**: RGB(35, 55, 75) - Fundo do logo
- **Yellow-Orange**: RGB(255, 200, 50) - Destaques digitais
- **White**: RGB(255, 255, 255) - Bordas e contornos

## Personalizando os ícones

Para personalizar cores, dimensões ou elementos do design, edite o arquivo `create_icons.py`:

- Modifique os valores RGB para mudar cores
- Altere os valores de dimensões (256x256, 512x128) para redimensionar
- Ajuste as coordenadas das formas para mudar o design

## Integração com Home Assistant

Depois de gerar os ícones:

1. Coloque `icon.png` na raiz do diretório do addon ou em um subdiretório apropriado
2. Configure o caminho do ícone no `config.yaml` do addon se necessário
3. Para `logo.png`, use em documentação README ou página de apresentação do addon

## Troubleshooting

### Erro: "ModuleNotFoundError: No module named 'PIL'"
Instale Pillow:
```bash
pip install Pillow
```

### Ícones com qualidade ruim
Certifique-se de usar arquivos PNG com as dimensões corretas (256x256 para icon.png e 512x128 para logo.png).

## Notas

- Os ícones são gerados com transparência (RGBA)
- Compatível com sistemas Linux, macOS e Windows
- O script pode ser integrado com CI/CD para gerar automaticamente os ícones
