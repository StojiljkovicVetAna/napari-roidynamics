import numpy as np

from napari_roidynamics._widget import RoidynamicsforNapari

# make_napari_viewer is a pytest fixture that returns a napari viewer object
# capsys is a pytest fixture that captures stdout and stderr output streams
def test_example_q_widget(make_napari_viewer, capsys):
    # make viewer and add an image layer using our fixture
    viewer = make_napari_viewer()
    viewer.add_image(np.random.random((100, 100)))

    # create our widget, passing in the viewer
    my_widget = RoidynamicsforNapari(viewer)

    my_widget._ROI_click()
    viewer.layers['point of interest'].data = [[50,50]]

    #call our widget method
    my_widget._on_click_radial()

    assert 'radial_mask' in viewer.layers, "radial_mask layer not added"
