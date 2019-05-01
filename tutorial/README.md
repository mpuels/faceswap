# Tutorial: Swap Faces of Cage and Trump

    $ install-debs.sh
    $ # install packages from requirements.txt. See below for details.
    $ download-videos.sh
    $ extract-frames.sh
    $ extract-faces.sh

## Install packages from requirements.txt

### Local Machine

Set up a virtual environment on your local machine to be able to browse the code
with an IDE (e.g. PyCharm):

    $ pushd .. && make venv && popd

### EC2 Instance (DLAMI)

On an DLAMI on AWS, activate a Python environment that has support for
TensorFlow and then install the packages from `requirements.txt`:

    $ pushd ..
    $ source …
    $ pip install -r requirements.txt
