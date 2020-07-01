from django.shortcuts import render
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import Button
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.sampledata.sea_surface_temperature import sea_surface_temperature
from bokeh.embed import server_document

@login_required()
def home(request):
    script = server_document(request.build_absolute_uri())
    context = {'script': script}
    return render(request, 'bokeh_tutorial/home.html', context)


def home_handler(documnet):
    df = sea_surface_temperature.copy()
    source = ColumnDataSource(data=df)

    plot = figure(x_axis_type="datatime", y_range=(0, 25), y_axis_label="Temperature (Celcius)",
                  height=500, width=800, title="Sea Surface Temperature at 43.18, -70.43")
    plot.line("time", "temperature", source=source)

    document.add_root(plot)