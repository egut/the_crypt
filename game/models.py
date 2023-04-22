"""
    Defines the game setup.

"""

from django.conf import settings
from django.db import models

# Create your models here.


class GameConfig(models.Model):
    """
    This is the model that connects the game together.

    This describes how one game type is configured, this can be "standard Werewolf"

    Args:
        models (_type_): _description_
    """
    name = models.CharField(
        max_length=100,
        help_text="The name of the game configuration",
        unique=True)

    def __str__(self):
        return str(self.__unicode__())

    def __unicode__(self):
        return self.name


class Game(models.Model):
    """
    This is the model that connects the game together.

    Args:
        models (_type_): _description_
    """
    name = models.CharField(
        max_length=100,
        help_text="The name of the game",
        unique=True)

    game_config = models.ForeignKey(
        GameConfig,
        on_delete=models.CASCADE)

    start_time = models.DateTimeField(
        help_text="When the game will start")

    def __str__(self):
        return str(self.__unicode__())

    def __unicode__(self):
        return self.name


class Player(models.Model):
    """
    This will define the player in the game.

    Args:
        models (_type_): _description_
    """

    #How is the real player
    user = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE)

    #To what game do this relate to
    game = models.OneToOneField(
        Game,
        on_delete=models.CASCADE)

   #To what figure set this player have.
    figure_set = models.OneToOneField(
        "FigureSet",
        blank=True,
        on_delete=models.CASCADE)

    #The name in the game
    name = models.CharField(
        help_text="Vad vill du kalla dig i detta spelet?",
        max_length=50,
        blank=False)

    # Todo: Follow https://djangocentral.com/uploading-images-with-django/
    profile = models.ImageField(
        upload_to='profiles')

    health = models.IntegerField(
        default=100)

    def __str__(self):
        return str(self.__unicode__())

    def __unicode__(self):
        return self.name


class FigureSet(models.Model):
    """
    A player may have one or more figures to play with,
    this define a set of figures to use.
    """

    #The name of the set
    name = models.CharField(
        max_length=50,
        blank=False)

    def __str__(self):
        return str(self.__unicode__())


    def __unicode__(self):
        return self.name


class Phalanx(models.Model):
    """
    All action, effects, and victory conditions are linked
    to the phalanx that are in play.

    A phalanx my have a parent and then it inherit
    all the from its parent too

    """
    game_config = models.ForeignKey(
        GameConfig,
        null=True,
        blank=True,
        on_delete=models.CASCADE)

    parent_phalanx = models.ForeignKey(
        "Phalanx",
        null = True,
        blank = True,
        on_delete=models.CASCADE)

    name = models.CharField(
        max_length=50,
        help_text="The name of the phalanx")

    description = models.TextField(blank=True)

    def __str__(self):
        return str(self.__unicode__())

    def __unicode__(self):


        if self.parent_phalanx:
            return f'{self.parent_phalanx}/{self.name} ({self.game_config})'
        return f'{self.name} ({self.game_config}) '




class Figure(models.Model):
    """

    Describe one figure in the game, a player my have one or more
    figures linked to them self.

    """
    title = models.CharField(
        max_length=50,
        blank=False,
        help_text="The name of the figure")

    description = models.TextField(
        help_text="Description of the figure"
    )

    image =  models.ImageField(
        upload_to='figures',
        blank=True)


    # What figure set a figure belongs to
    # A player can only be associated with a set
    figure_set = models.ManyToManyField(
        to=FigureSet,
        blank=True
    )

    #What phalanx a figure belongs to, this is where all the rest is defined.
    phalanx = models.ForeignKey(
        Phalanx,
        on_delete=models.CASCADE
    )

    FigureType = models.TextChoices(
        'FigureType', 'PROFESSION PERSONA ALONE')
    type = models.CharField(
        choices=FigureType.choices,
        max_length=20,
        help_text="What kind of figure is this?")

    def __str__(self):
        return str(self.__unicode__())

    def __unicode__(self):
        return self.title


class Action(models.Model):
    """

    What action this phalanx have,
    some phalanx need to be only one player.

    """
    phalanx = models.ForeignKey(
        Phalanx,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=20)

    number_of_usage = models.IntegerField()

    ActionType = models.TextChoices(
        'ActionType', 'ATTACK DEFENSE LOOKUP')
    type = models.CharField(
        choices=ActionType.choices,
        max_length=20,
        help_text="What kind of action?")

    #Strange of the attack
    value = models.IntegerField()

    # Define when this action is valid and happens.
    # requires = models.CharField()

    def __str__(self):
        return str(self.__unicode__())

    def __unicode__(self):
        return self.phalanx + ' ' + self.name


class Effect(models.Model):
    """

    An effect is something that happens when this figure have been attacked

    """
    figure = models.OneToOneField(
        Figure,
        on_delete=models.CASCADE)

    name = models.CharField(max_length=20)

    number_of_usage = models.IntegerField()

    ActionType = models.TextChoices(
        'ActionType', 'ATTACK DEFENSE LOOKUP')
    type = models.CharField(
        choices=ActionType.choices,
        max_length=20,
        help_text="What kind of action?")

    #Strange of the attack
    value = models.IntegerField()

    # Define when this action is valid and happens.
    # requires = models.CharField()

    def __str__(self):
        return str(self.__unicode__())

    def __unicode__(self):
        return self.figure + ' ' + self.name


class Victory(models.Model):
    """
    Condition to win!

    """
    phalanx = models.name = models.ForeignKey(
        Phalanx,
        on_delete=models.CASCADE,
        help_text="To what phalanx is this win condition for")

    name = models.CharField(
        max_length=200,
        blank=False)

    WinConditionBase = models.TextChoices(
        'WinConditionBase', 'ALL_OTHER PHALANX')
    win_condition = models.CharField(
        choices=WinConditionBase.choices,
        max_length=20,
        help_text="What kind of win condition?")

    win_condition_argument = models.OneToOneField(
        Phalanx,
        on_delete=models.CASCADE,
        related_name="+",
        help_text="How do it relate to, if any?")

    def __str__(self):
        return str(self.__unicode__())

    def __unicode__(self):
        return self.name
