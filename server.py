from flask import Flask
from flask import render_template,request
from model import run_model

app = Flask(__name__)

@app.route("/")
def init():
    p_type = ['Jovian', 'Neptunian', 'Superterran', 'Terran', 'Subterran','Miniterran']
    temp_ptype = ['Hot', 'Cold', 'Warm']
    const_name =['Scorpius', 'Cygnus', 'Lyra', 'Pisces', 'Ursa Major', 'Ophiuchus',
       'Leo', 'Cetus', 'Libra', 'Draco', 'Hydrus', 'Aquarius', 'Carina',
       'Eridanus', 'Cassiopeia', 'Caelum', 'Canes Venatici', 'Aquila',
       'Crater', 'Sagittarius', 'Taurus', 'Hercules', 'Hydra', 'Lynx',
       'Lepus', 'Cancer', 'Virgo', 'Bootes', 'Lupus', 'Orion',
       'Centaurus', 'Microscopium', 'Lacerta', 'Phoenix', 'Pavo',
       'Tucana', 'Pyxis', 'Andromeda', 'Auriga', 'Dorado', 'Puppis',
       'Horologium', 'Pegasus', 'Equuleus', 'Indus', 'Canis Major',
       'Sculptor', 'Columba', 'Mensa', 'Octans', 'Aries',
       'Corona Borealis', 'Perseus', 'Sextans', 'Serpens', 'Canis Minor',
       'Ursa Minor', 'Capricornus', 'Volans', 'Grus', 'Monoceros', 'Vela',
       'Gemini', 'Antlia', 'Pictor', 'Circinus', 'Cepheus',
       'Corona Australis', 'Telescopium', 'Apus', 'Coma Berenices',
       'Sagitta', 'Vulpecula', 'Delphinus', 'Fornax', 'Camelopardalis',
       'Triangulum', 'Corvus', 'Leo Minor', 'Reticulum', 'Musca',
       'Piscis Austrinus', 'Norma', 'Scutum', 'Ara',
       'Triangulum Australe', 'Chamaeleon', 'Crux']
    
    return render_template('index.html',p_type=p_type,temp_ptype=temp_ptype,const_name=const_name)

@app.route("/res",methods=['POST'])
def prediction():
    
    if request.method == 'POST':
        print(request.form)
    
    res =run_model(request.form)
        
    # print(request.args.get('param'))
    if res == 0: 
        out =  render_template('res.html',message = "There is no life",path='static/img/no.jpg')
    elif res == 1:
        out = render_template('res.html',message = "There maybe life",path='static/img/yes.jpg')
    elif res == 2:
        out = render_template('res.html',message = "There is life",path='static/img/yes.jpg')
    else:
        out = "<H1>404 not found</h1>"
    
    return out