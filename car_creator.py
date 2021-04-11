def make_car(manufacturer, model, **kwargs):
    """Store info about a car"""
    kwargs['car_make'] = manufacturer
    kwargs['car_model'] = model
    return kwargs
