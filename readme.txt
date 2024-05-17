DNS Spoofing Program

ensure that the following is downloaded:
sudo apt-get install build-essential python-dev libnetfilter-queue-dev
sudo apt install libnetfilter-queue-dev
sudo git clone https://github.com/fqrouter/python-netfilterqueue.git
cd python-netfilterqueue
sudo python setup.py install

Run a web server: sudo service apache2 start

Run the code: python2.7 spoof.py

Now whenever you head to the target (www.google.com) website you'll be redirected to kali's server @ 10.0.2.15



