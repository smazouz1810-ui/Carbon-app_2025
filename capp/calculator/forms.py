from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, FloatField
from wtforms.validators import InputRequired


class BusForm(FlaskForm):
    kms = FloatField('Kilometers', [InputRequired()])
    fuel_type = SelectField(
        'Type of Fuel', [InputRequired()],
        choices=[
            ('Diesel', 'Diesel'), ('Biofuel HVO100', 'Biofuel HVO100'), ('Biofuel FAME100', 'Biofuel FAME100')])
    submit = SubmitField('Submit')


class CarForm(FlaskForm):
    kms = FloatField('Kilometers', [InputRequired()])
    fuel_type = SelectField(
        'Type of Fuel', [InputRequired()],
        choices=[
            ('Diesel', 'Diesel'), ('Gasoline', 'Gasoline'), ('Electricity Nordic', 'Electricity Nordic'), ('Fossil gas', 'Fossil gas'),
            ('Vehicle gas', 'Vehicle gas'), ('Biogas', 'Biogas'), ('Ethanol', 'Ethanol'),])
    vehicle_size = SelectField(
        'Vehicle Size', [InputRequired()],
        choices=[
            ('Small', 'Small car'), ('Medium', 'Medium car'), ('Large', 'Large car'), ('Camper', 'Camper / Caravan')])
    submit = SubmitField('Submit')



class TrainForm(FlaskForm):
    kms = FloatField('Kilometers', [InputRequired()])
    fuel_type = SelectField(
        'Type of Train', [InputRequired()],
        choices=[
            ('Electricity Nordic', 'Electricity Nordic'), ('Diesel', 'Diesel'), ('Biofuel HVO100', 'Biofuel HVO100')])
    submit = SubmitField('Submit')


class PlaneForm(FlaskForm):
    kms = FloatField('Distance (km)', [InputRequired()])
    ground_dep = FloatField('Distance to departure airport (km)', [InputRequired()])
    ground_arr = FloatField('Distance from arrival airport (km)', [InputRequired()])
    flight_type = SelectField(
        'Flight Type', [InputRequired()],
        choices=[('Scheduled', 'Scheduled flight'), ('Charter', 'Charter flight')]
    )
    seat_class = SelectField(
        'Seat Class', [InputRequired()],
        choices=[('Economy', 'Economy'), ('Premium', 'Premium'), ('Business', 'Business')]
    )
    submit = SubmitField('Submit')




class FerryForm(FlaskForm):
    kms = FloatField('Kilometers', [InputRequired()])
    fuel_type = SelectField(
        'Ferry Type', [InputRequired()],
        choices=[
            ('Standard fuel', 'Ferry – Standard fuel')])
    submit = SubmitField('Submit')


class MotorcycleForm(FlaskForm):
    kms = FloatField('Kilometers', [InputRequired()])
    fuel_type = SelectField(
        'Motorcycle Size', [InputRequired()],
        choices=[
            ('Small', 'Small motorcycle (<125cc)'), ('Medium', 'Medium motorcycle (125–500cc)'), ('Large', 'Large motorcycle (>500cc)')])
    submit = SubmitField('Submit')


