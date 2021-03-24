from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import stylecloud



st.set_option('deprecation.showPyplotGlobalUse', False)


st.sidebar.image("image.png",use_column_width=True)

# fonction pour definir le wordcloud
def cloud( text, max_word, max_font, random,colormap,background_color,gradient_direction,icon,size2,invert_mask):
    stopwords = set(STOPWORDS)
    stopwords.update(['us', 'one', 'will', 'said', 'now', 'well', 'man', 'may',
    'little', 'say', 'must', 'way', 'long', 'yet', 'mean',
    'put', 'seem', 'asked', 'made', 'half', 'much',
    'certainly', 'might', 'came',"a","à","â","abord",
    "afin","ah","ai","aie","ainsi","allaient","allo","allô","allons","après",
"assez","attendu","au","aucun","aucune","aujourd","aujourd'hui","auquel","aura",
"auront","aussi","autre","autres","aux","auxquelles","auxquels","avaient",
"avais","avait","avant","avec","avoir","ayant","b","bah","beaucoup","bien","bigre",
"boum","bravo","brrr","c","ça","car","ce","ceci","cela",
"celle","celle-ci","celle-là","celles","celles-ci","celles-là","celui","celui-ci","celui-là","cent",
"cependant","certain","certaine","certaines","certains","certes","ces","cet","cette","ceux","ceux-ci",
"ceux-là","chacun","chaque","cher","chère","chères","chers","chez","chiche","chut","ci","cinq","cinquantaine"
,"cinquante","cinquantième","cinquième","clac","clic","combien","comme","comment","compris","concernant"
,"contre","couic","crac","d","da","dans","de","debout","dedans","dehors","delà","depuis","derrière","des",
"dès","désormais","desquelles","desquels","dessous","dessus","deux","deuxième","deuxièmement","devant","devers"
,"devra","différent","différente","différentes","différents","dire","divers","diverse","diverses","dix",
"dix-huit","dixième","dix-neuf","dix-sept","doit","doivent","donc","dont","douze","douzième","dring",
"du","duquel","durant","e","effet","eh","elle","elle-même","elles","elles-mêmes","en","encore",
"entre","envers","environ","es","ès","est","et","etant","étaient","étais","était","étant","etc",
"été","etre","être","eu","euh","eux","eux-mêmes","excepté","f","façon","fais","faisaient","faisant",
"fait","feront","fi","flac","floc","font","g","gens","h","ha","hé","hein","hélas","hem","hep","hi",
"ho","holà","hop","hormis","hors","hou","houp","hue","hui","huit","huitième","hum","hurrah","i","il",
"ils","importe","j","je","jusqu","jusque","k","l","la","là","laquelle","las","le","lequel","les","lès",
"lesquelles","lesquels","leur","leurs","longtemps","lorsque","lui","lui-même","m","ma","maint","mais",
"malgré","me","même","mêmes","merci","mes","mien","mienne","miennes","miens","mille","mince","moi","moi-même",
"moins","mon","moyennant","n","na","ne","néanmoins","neuf","neuvième","ni","nombreuses","nombreux","non","nos",
"notre","nôtre","nôtres","nous","nous-mêmes","nul","o","o|","ô","oh","ohé","olé","ollé","on","ont","onze","onzième",
"ore","ou","où","ouf","ouias","oust","ouste","outre","p","paf","pan","par","parmi","partant","particulier",
"particulière","particulièrement","pas","passé","pendant","personne","peu","peut","peuvent","peux","pff",
"pfft","pfut","pif","plein","plouf","plus","plusieurs","plutôt","pouah","pour","pourquoi","premier","première",
"premièrement","près","proche","psitt","puisque","q","qu","quand","quant","quanta","quant-à-soi","quarante",
"quatorze","quatre","quatre-vingt","quatrième","quatrièmement","que","quel","quelconque","quelle","quelles",
"quelque","quelques","quelqu'un","quels","qui","quiconque","quinze","quoi","quoique","r","revoici","revoilà",
"rien","s","sa","sacrebleu","sans","sapristi","sauf","se","seize","selon","sept","septième","sera","seront",
"ses","si","sien","sienne","siennes","siens","sinon","six","sixième","soi","soi-même","soit","soixante","son",
"sont","sous","stop","suis","suivant","sur","surtout","t","ta","tac","tant","te","té","tel","telle","tellement",
"telles","tels","tenant","tes","tic","tien","tienne","tiennes","tiens","toc","toi","toi-même","ton","touchant",
"toujours","tous","tout","toute","toutes","treize","trente","très","trois","troisième","troisièmement","trop",
"tsoin","tsouin","tu","u","un","une","unes","uns","v","va","vais","vas","vé","vers","via","vif","vifs","vingt",
"vivat","vive","vives","vlan","voici","voilà","vont","vos","votre","vôtre","vôtres","vous","vous-mêmes","vu",
"w","x","y","z","zut","alors","aucuns","bon","devrait","dos","droite","début","essai","faites","fois","force",
"haut","ici","juste","maintenant","mine","mot","nommés","nouveaux","parce","parole","personnes","pièce",
"plupart","seulement","soyez","sujet","tandis","valeur","voie","voient","état","étions"])



   # import pandas as pd
    # on transfrom l'input en list puis en dataframe puis on crée un csv
    #mood = [text]
    #df = pd.DataFrame(mood)
    #df.to_csv('file.csv',index=False)
   # size = str(width)str(height)
    inv_mask = False
    gradient = None
    if size2 == 'square':
       size = (512,512)
    if size2 == 'rectangle':
       size = (1024,512)
    if invert_mask == "Yes":
        inv_mask = True
    if gradient_direction is not None:
        gradient = gradient_direction
        
    
    # generate the style cloud
    stylecloud.gen_stylecloud(text=text,
                          custom_stopwords=stopwords,
    background_color=background_color,
    random_state=random,
    max_words=max_word,
    max_font_size = max_font,
    palette = 'cartocolors.qualitative.{}'.format(colormap),
    #gradient= gradient,
    invert_mask = inv_mask,
    icon_name = 'fas fa-{}'.format(icon),
    
    size = size)
    
    st.image('stylecloud.png')
    
   


def main():
    st.write("# Generate Awesome Wordcloud !")
    st.write("[By Régis Amon](https://www.linkedin.com/in/r%C3%A9gis-amon-87669665/)")
    st.write("[Using the Stylecloud library created by Minimaxir](https://github.com/minimaxir/stylecloud)")
    max_word = st.sidebar.slider("Max words", 200, 3000, 200)
    max_font = st.sidebar.slider("Max Font Size", 50, 350, 60)
    random = st.sidebar.slider("Random State", 30, 100, 42 )
    size2 = st.sidebar.selectbox("Which size",['square','rectangle'])

    
    
    gradient_direction = None
   # gradient = st.sidebar.radio("Gradient ?",('Non','Oui'))
   # if gradient == 'Oui':
    #    gradient_direction = st.sidebar.selectbox("Orientation du gradient",["horizontal"])
    
    text = st.text_area("Copy-Paste some text here...")
    # ajout de couleur
    colormap = st.sidebar.selectbox("Palette ?",["Bold_5","Pastel_6","Safe_7","Vivid_8"])
    background_color=st.sidebar.selectbox("Background Color ?",["white","black"])
    icon = st.sidebar.selectbox("Icon ?",["flag","at","cloud","user","angle-right","angle-double-right","mask","calendar-check"
                                               ,"balance-scale","battery-full","bell","birthday-cake","search","tag",
                                               "book-reader","chart-line","coffee","comment","comments","tshirt","bullseye"
                                               ,"cube","cubes","expand-arrows-alt,""facebook","mug-hot",
                                               "glass-martini","globe-africa","grin","grin-hearts","graduation-cap","laugh"
                                               ,"microphone","paper-plane","lock-open","percent"])
    invert_mask = st.sidebar.selectbox("Invert mask ?",["No","Yes"])
    if text is not None:
        if st.button("Generate Wordcloud"):
          
       
            st.write("### Word cloud")
            st.write(cloud(text, max_word, max_font, random,colormap,background_color,gradient_direction,icon,size2,invert_mask), use_column_width=True)

    
if __name__=="__main__":
    main()
