from flask import render_template, Blueprint, redirect, url_for, flash, abort
from capp.models import Transport
from capp import db
from flask_login import current_user, login_required
from capp.calculator.forms import BusForm, CarForm, PlaneForm, TrainForm, FerryForm, MotorcycleForm
from datetime import datetime, timedelta

calculator = Blueprint('calculator', __name__)


fco2 = {

    "Car": {
        "Diesel":     {"Small": 58,  "Medium": 76,  "Large": 101, "Camper": 149},
        "Gasoline":   {"Small": 50,  "Medium": 66,  "Large": 87,  "Camper": 129},
        "Electricity Nordic": {"Small": 15, "Medium": 20, "Large": 26, "Camper": 36},
        "Fossil gas": {"Small": 51,  "Medium": 68,  "Large": 89,  "Camper": 132},
        "Vehicle gas": {"Small": 6.8, "Medium": 9.0, "Large": 12, "Camper": 18},
        "Biogas":     {"Small": 6.6, "Medium": 8.6, "Large": 11, "Camper": 17},
        "Ethanol":    {"Small": 23,  "Medium": 31,  "Large": 40, "Camper": 60}
    },

    "Bus": {
        "Diesel": 30,
        "Biofuel HVO100": 3.5,
        "Biofuel FAME100": 11
    },

    "Train": {
        "Electricity Nordic": 7,
        "Diesel": 91,
        "Biofuel HVO100": 10
    },

    "Ferry": {
        "Standard fuel (186)": 186,
        "Standard fuel (377)": 377
    },

    "Motorcycle": {
        "Small": 85.0,
        "Medium": 103.2,
        "Large": 137.2
    },

    "Plane": {
        "Scheduled": {
            "Standard fuel": {"Economy": 127, "Premium": 155, "Business": 284},
            "100% biofuel": {"Economy": 51, "Premium": 63, "Business": 115}
        },
        "Charter": {
            "Standard fuel": {"Economy": 112, "Premium": 137},
            "100% biofuel": {"Economy": 45, "Premium": 56}
        }
    }
}




@calculator.route('/calculator', methods=['GET'])
@login_required
def calculator_home():
    return render_template('calculator/calculator_home.html', title='Calculator')



@calculator.route('/calculator/new_entry_car', methods=['GET', 'POST'])
@login_required
def new_entry_car():
    form = CarForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        size = form.vehicle_size.data

        factor = fco2["Car"][fuel][size]
        total = kms * factor

        entry = Transport(
            kms=kms,
            transport="Car",
            fuel=f"{fuel} ({size})",
            total=round(total, 2),
            author=current_user
        )

        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('calculator.your_data'))

    return render_template('calculator/new_entry_car.html', title="Car Calculator", form=form)



@calculator.route('/calculator/new_entry_bus', methods=['GET', 'POST'])
@login_required
def new_entry_bus():
    form = BusForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data

        factor = fco2["Bus"][fuel]
        total = kms * factor

        entry = Transport(
            kms=kms,
            transport="Bus",
            fuel=fuel,
            total=round(total, 2),
            author=current_user
        )

        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('calculator.your_data'))

    return render_template('calculator/new_entry_bus.html', title="Bus Calculator", form=form)



@calculator.route('/calculator/new_entry_train', methods=['GET', 'POST'])
@login_required
def new_entry_train():
    form = TrainForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data

        factor = fco2["Train"][fuel]
        total = kms * factor

        entry = Transport(
            kms=kms,
            transport="Train",
            fuel=fuel,
            total=round(total, 2),
            author=current_user
        )

        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('calculator.your_data'))

    return render_template('calculator/new_entry_train.html', title="Train Calculator", form=form)



@calculator.route('/calculator/new_entry_ferry', methods=['GET', 'POST'])
@login_required
def new_entry_ferry():
    form = FerryForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data

        factor = fco2["Ferry"][fuel]
        total = kms * factor

        entry = Transport(
            kms=kms,
            transport="Ferry",
            fuel=fuel,
            total=round(total, 2),
            author=current_user
        )

        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('calculator.your_data'))

    return render_template('calculator/new_entry_ferry.html', title="Ferry Calculator", form=form)




@calculator.route('/calculator/new_entry_motorcycle', methods=['GET', 'POST'])
@login_required
def new_entry_motorcycle():
    form = MotorcycleForm()
    if form.validate_on_submit():
        kms = form.kms.data
        size = form.fuel_type.data 

        factor = fco2["Motorcycle"][size]
        total = kms * factor

        entry = Transport(
            kms=kms,
            transport="Motorcycle",
            fuel=size,
            total=round(total, 2),
            author=current_user
        )

        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('calculator.your_data'))

    return render_template('calculator/new_entry_motorcycle.html', title="Motorcycle Calculator", form=form)


@calculator.route('/calculator/new_entry_plane', methods=['GET', 'POST'])
@login_required
def new_entry_plane():
    form = PlaneForm()
    if form.validate_on_submit():
        kms = form.kms.data
        ground_dep = form.ground_dep.data
        ground_arr = form.ground_arr.data
        flight_type = form.flight_type.data
        seat_class = form.seat_class.data

        fuel_type = "Standard fuel"  # par défaut

        factor = fco2["Plane"][flight_type][fuel_type][seat_class]
        total = (kms * factor) + (ground_dep + ground_arr) * 44

        entry = Transport(
            kms=kms,
            transport="Plane",
            fuel=f"{fuel_type} ({flight_type}/{seat_class})",
            total=round(total, 2),
            author=current_user
        )

        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('calculator.your_data'))

    return render_template('calculator/new_entry_plane.html', title="Plane Calculator", form=form)



@calculator.route('/calculator/your_data')
@login_required
def your_data():
    five_days_ago = datetime.now() - timedelta(days=5)

    entries = (
        Transport.query
        .filter_by(user_id=current_user.id)
        .filter(Transport.date > five_days_ago)
        .order_by(Transport.date.desc())
        .all()
    )


    transports_list = ['Bus', 'Car', 'Train', 'Ferry', 'Motorcycle', 'Plane']


    emissions_by_transport = db.session.query(
        db.func.sum(Transport.total), Transport.transport
    ).filter(
        Transport.date > five_days_ago, Transport.user_id == current_user.id
    ).group_by(Transport.transport).all()

    emission_transport_dict = {t: 0 for t in transports_list}
    for total, transport in emissions_by_transport:
        emission_transport_dict[transport] = float(total)

   
    kms_by_transport = db.session.query(
        db.func.sum(Transport.kms), Transport.transport
    ).filter(
        Transport.date > five_days_ago, Transport.user_id == current_user.id
    ).group_by(Transport.transport).all()

    kms_transport_dict = {t: 0 for t in transports_list}
    for total, transport in kms_by_transport:
        kms_transport_dict[transport] = float(total)


    emissions_by_date = db.session.query(
        db.func.sum(Transport.total), Transport.date
    ).filter(
        Transport.date > five_days_ago, Transport.user_id == current_user.id
    ).group_by(db.func.date(Transport.date)).order_by(Transport.date.asc()).all()

    over_time_emissions = []
    dates_label = []
    for total, date in emissions_by_date:
        over_time_emissions.append(float(total))
        dates_label.append(date.strftime('%m-%d-%Y'))

   
    kms_by_date = db.session.query(
        db.func.sum(Transport.kms), Transport.date
    ).filter(
        Transport.date > five_days_ago, Transport.user_id == current_user.id
    ).group_by(db.func.date(Transport.date)).order_by(Transport.date.asc()).all()

    over_time_kms = []
    for total, date in kms_by_date:
        over_time_kms.append(float(total))

    return render_template(
        'calculator/your_data.html',
        title='Your Data',
        entries=entries,
        transports=transports_list,
        emission_transport=list(emission_transport_dict.values()),
        kms_transport=list(kms_transport_dict.values()),
        over_time_emissions=over_time_emissions,
        over_time_kms=over_time_kms,
        dates_label=dates_label
    )


@calculator.route('/calculator/delete_emissions/<int:entry_id>')
@login_required
def delete_emissions(entry_id):
    entry = Transport.query.get_or_404(entry_id)

    if entry.user_id != current_user.id:
        abort(403)

    db.session.delete(entry)
    db.session.commit()

    flash('Entry deleted!', 'success')
    return redirect(url_for('calculator.your_data'))
