{% load thumbnail %}

[{% for trainer in object_list %}{% thumbnail trainer.profile_picture "250x250" crop="center" as im %}
    {"im":"{{ im.url }}",
        "meta": {
            "": "{{ trainer.first_name }}{{ trainer.last_name }}",
            "LC: ": "{{trainer.lc}}",
            "Trainings delivered: ":"{{trainer.trainings_delivered}}",
            "Speaks: ": "{{trainer.languages}}",
            "Contact: ":"{{trainer.contact}}",
            "Favourite Trainings: ":"{{trainer.preferred_topics}}"
        }
    },
    {% endthumbnail %}{% endfor %}{"im":"None"}]
