import os


class DocGen:
    # DEPENDÊNCIAS ----------------------------------------------------------------------------------------------------
    def __isiterable(self, obj):
        try:
            iter(obj)
            return True
        except TypeError:
            return False
    
    # CONSTRRUTOR DO OBJETO --------------------------------------------------------------------------------------------------------------------
    def __init__(self, title, font_family=0, lang="pt-br"):
        self.__path = os.getcwd() # f"OUTPUT/HTML/{title}.html"
        self.__lang = lang
        self.__title = title
        self.__body = []
        self.__style = {}
        if font_family == 0:
            self.__set_style_param('body', 'font-family', 'Arial, Helvetica, sans-serif')
        else:
            self.__set_style_param('body', 'font-family', '"Times New Roman", Times, serif')


    # SEÇÃO DE CONFIGURAÇÃO -------------------------------------------------------------------------------------------------------------------------
    def set_title(self, title):
        self.__title = title
        self.__path = f"OUTPUT/HTML/{title}.html"
        
        
    # SEÇÃO DE ESTILIZAÇÃO -----------------------------------------------------------------------------------------------------------------------
    def __set_style_param(self, tag, selector, value):
        if tag in self.__style:
            self.__style[tag][selector] = value
        else:
            self.__style[tag] = {selector: value}
    
    
    def set_background_color(self, color):
        self.__style['body']['background-color'] = color
    def set_font_color(self, color):
        self.set_p_font_color(color)
        self.set_h_font_color(range(1,7), [color]*6)
        self.set_list_font_color(color)
        self.set_table_font_color(color)
        
        
    def set_p_font_color(self, color):
        self.__style['p']['color'] = color      
    def set_p_text_align(self, align):
        self.__set_style_param('p', 'text-align', align)
    def set_p_font_size(self, size="10pt"):
        self.__set_style_param('p', 'font-size', size)
    def set_p_identation(self, identation, unit="cm"):
        self.__set_style_param('p', 'text-indent', str(identation) + unit)
    
    
    def set_h_font_color(self, level, color):
        if not self.__isiterable(level):
            level = [level]
        if not self.__isiterable(color):
            color = [color]
        if len(level) == len(color):
            for i in range(len(level)):
                if level[i] in range(1, 7):
                    self.__set_style_param('h' + str(level[i]), 'color', color[i])
                else:
                    print("\nCHANGING HEADING COLOR ERROR:\nInvalid level")
    def set_h_font_size(self, level, size, unit="pt"):
        if not self.__isiterable(level):
            level = [level]
        if not self.__isiterable(size):
            size = [size]
        if len(level) == len(size):
            for i in range(len(level)):
                if level[i] in range(1, 7):
                    self.__set_style_param('h' + str(level[i]), 'font-size', str(size[i]) + unit)
                else:
                    print("\nCHANGING HEADING FONT SIZE ERROR:\nInvalid level")
        else:
            print("\nCHANGING HEADING FONT SIZE ERROR:\nLevels and sizes do not match")
    def set_h_text_align(self, level, align):
        if level in range(1, 7):
            self.__set_style_param('h' + str(level), 'text-align', align)
        else:
            print("\nCHANGING HEADING TEXT ALIGN ERROR:\nInvalid level")


    def set_list_font_color(self, color):
        if 'li' in self.__style:
            self.__style['li']['color'] = color
        else:
            self.__style['li'] = {'color': color}     
    def set_font_family(self, font_family):
        if font_family == 0:
            self.__style['body']['font-family'] = 'Arial, Helvetica, sans-serif'
        elif font_family == 1:
            self.__style['body']['font-family'] = '"Times New Roman", Times, serif'
        else: 
            self.__style['body']['font-family'] = font_family
            
    
    def set_th_table_font_color(self, color):
        self.__set_style_param("th", "color", color)
    def set_th_table_font_size(self, size="12pt"):
        self.__set_style_param("th", "font-size", size)
    def set_th_table_font_family(self, font_family=0):
        if font_family == 0:
            self.__set_style_param("th", "font-family", "Arial, Helvetica, sans-serif")
        elif font_family == 1:
            self.__set_style_param("th", "font-family", '"Times New Roman", Times, serif')
        else:
            self.__set_style_param("th", "font-family", font_family)
    def set_th_table_border(self, width="1pt", style="Solid", color="black"):
        self.__set_style_param("th", "border", width + " " + style + " " + color)
    
    def set_td_table_font_color(self, color):
        try:
            self.__style['td']['color'] = color
        except KeyError:
            self.__style['td'] = {'color': color}
    def set_td_table_font_family(self, font_family=0):
        if font_family == 0:
            self.__set_style_param("td", "font-family", "Arial, Helvetica, sans-serif")
        elif font_family == 1:
            self.__set_style_param("td", "font-family", '"Times New Roman", Times, serif')
        else:
            self.__set_style_param("td", "font-family", font_family)
    def set_td_table_border(self, width="1pt", style="Solid", color="black"):
        self.__set_style_param("td", "border", width + " " + style + " " + color)
    def set_td_table_font_size(self, size="10pt"):
        self.__set_style_param("td", "font-size", size)
    
    def set_caption_table_font_color(self, color):
        try:
            self.__style['caption']['color'] = color
        except KeyError:
            self.__style['caption'] = {'color': color}
    def set_caption_table_font_family(self, font_family=0):
        if font_family == 0:
            self.__set_style_param("caption", "font-family", "Arial, Helvetica, sans-serif")
        elif font_family == 1:
            self.__set_style_param("caption", "font-family", '"Times New Roman", Times, serif')
        else:
            self.__set_style_param("caption", "font-family", font_family)
    def set_caption_table_font_size(self, size="8pt"):
        self.__set_style_param("caption", "font-size", size)
    def set_caption_table_font_style(self, style="italic"):
        self.__set_style_param("caption", "font-style", style)
    def set_caption_table_side(self, side="bottom"):
        self.__set_style_param("caption", "caption-side", "bottom")
    def set_caption_table_align(self, align="center"):
        self.__set_style_param("caption", "text-align", align)
    
    def set_table_font_color(self, color):
        self.set_th_table_font_color(color)
        self.set_td_table_font_color(color)
        self.set_caption_table_font_color(color)
    def set_table_external_border(self, width="1pt", style="Solid", color="black"):
        self.__set_style_param("table", "border", width + " " + style + " " + color)
    def set_table_border(self, width="1pt", style="Solid", color="black", collapse=True):
        self.set_th_table_border(width, style, color)
        self.set_td_table_border(width, style, color)
        self.set_table_external_border(width, style, color)
        self.__set_style_param("table", "border-collapse", "collapse") if collapse else self.__set_style_param("table", "border-collapse", "separate")
    def set_table_width(self, width="100%"):
        self.__set_style_param("table", "width", width)
    def set_table_font_size(self, th_size="12pt", td_size="10pt"):
        self.set_th_table_font_size(th_size)
        self.set_td_table_font_size(td_size)
    def set_table_font_family(self, font_family):
        self.set_th_table_font_family(font_family)
        self.set_td_table_font_family(font_family)
    
    
    # SEÇÃO DE INSERÇÃO DE CONTEÚDO ----------------------------------------------------------------------------------------------------------------
    def insert_p(self, text):
        self.__body.append(
            "    <p>" + text + "</p>"
        )
    def insert_section(self, text, _class=None):
        self.__body.append(
            f'    <section class={_class}>' + text + '</section>' 
        )
    def insert_h(self, level, text):
        if level in range(1, 7):
            self.__body.append(
                "    <h" + str(level) + ">" + text + "</h" + str(level) + ">"
            )
        else:
            print("\nHEADING WRITING ERROR:\nInvalid level")
    def insert_page_break(self):
        self.__body.append(
            '    <p style="page-break-after: always;"></p>'
        )
    def insert_img(self, src, width=100, unit="%"):
        try:
            self.__body.append(
                '    <img src="../..' + src + '" width="' + str(width) + unit + '" alt="Imagem não encontrada">'
            )
        except FileNotFoundError:
            print("\nIMAGE WRITING ERROR:\nFile not found")
        except TypeError:
            print("\nIMAGE WRITING ERROR:\nInvalid width ou unit")
        except Exception:
            print("\nIMAGE WRITING ERROR:\nUnknown error")
    def insert_list(self, list, ordered=False):
        if self.__isiterable(list):
            if ordered:
                self.__body.append(
                    "    <ol>\n" + "\n".join([f"        <li>{str(elem)}</li>" for elem in list]) + "\n    </ol>"
                )
            else:
                self.__body.append(
                    "    <ul>\n" + "\n".join([f"        <li>{str(elem)}</li>" for elem in list]) + "\n    </ul>"
                )
        else:
            print("\nLIST WRITING ERROR:\nInvalid list")
    def insert_table(self, table, heading=[], caption=""):
        if all(len(row) == len(table[0]) for row in table):    
            self.__body.append(" "*4 + "<table>")
            self.__body.append(" "*8 + "<caption>" + caption + "</caption>") if caption != "" else None
            
            if len(heading) > 0:
                if len(heading) != len(table[0]):
                    print("\nTABLE PLOTTING ERROR:\nNumber of columns in heading does not match number of columns")
                self.__body.append(" "*8 + "<tr>")
                for elem in heading:
                    self.__body.append(" "*12 + "<th>" + str(elem) + "</th>")
                self.__body.append(" "*8 + "</tr>")
                
            for row in table:
                self.__body.append(" "*8 + "<tr>")
                for elem in row:
                    self.__body.append(" "*12 + "<td>" + str(elem) + "</td>")
                self.__body.append(" "*8 + "</tr>")
            
            self.__body.append(" "*4 + "</table>")
        else:
            print("\nTABLE PLOTTING ERROR:\nInvalid table")


    # SEÇÃO DE EXPORTAÇÃO ----------------------------------------------------------------------------------------------------------------------------     
    def __print_style(self):
        self.__style_str = ""
        for selector in self.__style:
            self.__style_str += " "*8 +  selector + " {\n"
            for prop in self.__style[selector]:
                self.__style_str += " "*12 + prop + ": " + self.__style[selector][prop] + ";\n"
            self.__style_str += " "*8 + "}\n"
        return self.__style_str
    def exportHTML(self, filename=None):
        if filename is None:
            filename = f'{self.__title}.html'
        with open(f'{self.__path}/{filename}', "w") as f:
            f.writelines(
f"""<!DOCTYPE html>
<html lang="{self.__lang}">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.__title}</title>
    <style>
"""
+ self.__print_style() +
"""        @media print {
            body {
                width: 297mm;
                height: 210mm;
                margin: 25mm 25mm 25mm 25mm;
            }
        }
        
        @page {
            size: 210mm 297mm;
            margin: 25mm 25mm 25mm 25mm;
        }
    </style>
</head>
<body>
""" 
+ "\n".join(self.__body) +
"""
</body>
</html>
"""
        )


    def exportPDF(self, filename=None):
        if filename is None:
            filename = f'{self.__title}'
        self.exportHTML(f"{filename}_temp.html")
        print("\nConverting document do PDF...")
        path_pdf = f"{self.__path}/{self.__title}.pdf"
        os.system(f"wkhtmltopdf --enable-local-file-access {self.__path}/{self.__title}.html {path_pdf}")
        os.remove(f"{filename}_temp.html")
        print()

# if __name__ == "__main__":
#     import os
#     import pandas as pd
    
#     teste = DocGen("Teste")
    
#     teste.set_background_color("#000012")
#     teste.set_font_color("#FFFFFF")
#     teste.set_table_border(color="white")
#     teste.set_table_width("100%")
#     teste.set_caption_table_font_style()
    
    
#     teste.insert_h(1, "Título")
#     teste.insert_p("Texto é um conjunto de palavras e frases encadeadas que permitem interpretação e transmitem uma mensagem. É qualquer obra escrita em versão original e que constitui um livro ou um documento escrito. Um texto é uma unidade linguística de extensão superior à frase. Um texto é constituído por uma ou mais frases, que podem ser separadas por pontuação, e que podem ser compostas por palavras, símbolos, números, etc.")
#     teste.insert_h(2, "Subtítulo")
#     teste.insert_h(3, "Subsubtítulo")
#     teste.insert_img("/INPUT/IMG/110018.jpg")
#     teste.insert_list(['a', 'b', 'c', 'd', 'e', 'f'], ordered=True)
#     teste.insert_list(range(1, 10))
#     df = pd.DataFrame([[1,2,3], [4,5,6], [7,8,9], [10,11,12]], columns=['Coluna A', 'Coluna B', 'Coluna C'])
#     teste.insert_table(df.values, heading=df.columns, caption="Tabela de exemplo")
#     teste.exportHTML()
#     teste.exportPDF()