from PyQt6.QtWidgets import *
from gui import *


class Television(QMainWindow, Ui_television_window):

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Method for defining default values to variables used in below methods,
         as well as connecting button clicks to event methods
        """
        super().__init__()
        self.setupUi(self)

        self.__status = False
        self.__muted = False
        self.__volume = 0
        self.__channel = 0

        self.channel_images = {0: "gui images/national_geographic.png",
                               1: "gui images/history_channel.png",
                               2: "gui images/NBC.png",
                               3: "gui images/espn.png"}

        self.slider_channel.setVisible(False)
        self.slider_volume.setDisabled(True)

        self.button_power.clicked.connect(lambda: self.power())
        self.button_mute.clicked.connect(lambda: self.mute())
        self.button_channel_up.clicked.connect(lambda: self.channel_up())
        self.button_channel_down.clicked.connect(lambda: self.channel_down())
        self.button_volume_up.clicked.connect(lambda: self.volume_up())
        self.button_volume_down.clicked.connect(lambda: self.volume_down())
        self.slider_channel.valueChanged.connect(lambda: self.set_channel_slider_value())
        self.slider_volume.valueChanged.connect(lambda: self.set_volume_slider_value())

    def power(self) -> None:
        """
        This method turns the TV display on, unhides the channel slider,
        and enables/disables the volume slider if it is off, and turns the TV display off
        if the TV is on.
        """
        if self.__status:
            self.__status = False
            self.slider_channel.setVisible(False)
            self.slider_volume.setDisabled(True)
            self.label_television_display.setPixmap(QtGui.QPixmap("gui images/power_off.jpg"))
        else:
            self.__status = True
            self.slider_channel.setVisible(True)
            if self.__muted:
                self.slider_volume.setDisabled(True)
            else:
                self.slider_volume.setDisabled(False)
            self.channel_set_image()

    def mute(self) -> None:
        """
        This method controls the mute status as well as sets the mute label image based off of the value
        of self.__muted
        """
        if self.__status:
            if not self.__muted:
                self.button_mute.setIcon(QtGui.QIcon("gui images/unmuted.png"))
                self.slider_volume.setDisabled(True)
                self.__muted = True
            else:
                self.button_mute.setIcon(QtGui.QIcon("gui images/mute.png"))
                self.slider_volume.setDisabled(False)
                self.__muted = False

    def unmute(self) -> None:
        """
        This method is used for the volume changing methods and unmutes the TV if it is muted
        """
        self.__muted = False
        self.button_mute.setIcon(QtGui.QIcon("gui images/mute.png"))
        self.slider_volume.setDisabled(False)

    def channel_up(self) -> None:
        """
        This method increases the channel value by 1 and resets the value to the minimum if it reaches above
        the maximum
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
                self.channel_set_image()
            else:
                self.__channel = Television.MIN_CHANNEL
                self.channel_set_image()

    def channel_down(self) -> None:
        """
        This method decreases the channel value by 1 and resets the value to the maximum if it reaches below
        the minimum
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
                self.channel_set_image()
            else:
                self.__channel = Television.MAX_CHANNEL
                self.channel_set_image()

    def volume_up(self) -> None:
        """
        This method unmutes the TV and increases the volume value by 1
        """
        if self.__status:
            self.unmute()
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
                self.slider_volume.setValue(self.__volume)

    def volume_down(self) -> None:
        """
        This method unmutes the TV and decreases the volume value by 1
        """
        if self.__status:
            self.unmute()
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
                self.slider_volume.setValue(self.__volume)

    def set_channel_slider_value(self) -> None:
        """
        This method sets the channel value to the corresponding slider value if it is adjusted via
        arrow keys or scroll wheel
        """
        self.__channel = self.slider_channel.value()
        self.label_television_display.setPixmap(QtGui.QPixmap(self.channel_images[self.__channel]))

    def set_volume_slider_value(self) -> None:
        """
        This method sets the volume value to the corresponding slider value if it is adjusted via
        arrow keys or scroll wheel
        """
        self.__volume = self.slider_volume.value()

    def channel_set_image(self) -> None:
        """
        This method sets the TV display to a certain channel image corresponding to the channel value.
        It also sets the channel slider value based off the channel value
        """
        self.label_television_display.setPixmap(QtGui.QPixmap(self.channel_images[self.__channel]))
        self.slider_channel.setValue(self.__channel)
