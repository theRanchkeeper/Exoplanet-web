import joblib
import numpy as np

def run_model(inputs):
    
        loaded_encoders = joblib.load('lencoders.pkl')
        loaded_scaler = joblib.load('scaler.pkl')
        loaded_model = joblib.load('rf_model.pkl')


        p_mass = eval(inputs.get('mass-p'))
        p_rad = eval(inputs.get('radius'))
        s_mass = eval(inputs.get('mass-s'))
        p_escape = eval(inputs.get('ev'))
        p_potential = eval(inputs.get('gp'))
        p_density = eval(inputs.get('dp'))
        p_hill_sphere = eval(inputs.get('hsp'))
        p_flux_min = eval(inputs.get('minsf'))
        
        p_type = inputs.get('planet-type')
        p_type_temp = inputs.get('thermal-type')
        s_constellation = inputs.get('const-name')
        
        p_type = [p_type]
        p_type_temp = [p_type_temp]
        s_constellation = [s_constellation]
        

        p_type_encoder = loaded_encoders['P_TYPE']
        p_type_encoded = p_type_encoder.transform(p_type)

        p_type_temp_encoder = loaded_encoders['P_TYPE_TEMP']
        p_type_temp_encoded = p_type_temp_encoder.transform(p_type_temp)

        s_constellation_encoder = loaded_encoders['S_CONSTELLATION']
        s_constellation_encoded = s_constellation_encoder.transform(s_constellation)

        f_vect = [p_mass, p_rad, s_mass, p_escape, p_potential, p_density, p_hill_sphere, p_flux_min, p_type_encoded[0], p_type_temp_encoded[0], s_constellation_encoded[0]]
        print(f_vect)
        f_vect_reshaped = np.array(f_vect).reshape(1, -1)
        f_vect_scaled = loaded_scaler.transform(f_vect_reshaped)

        habitability_prediction = loaded_model.predict(f_vect_scaled)
        print(habitability_prediction,"predict")
        return habitability_prediction
            