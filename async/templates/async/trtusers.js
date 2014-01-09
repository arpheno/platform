{% load thumbnail %}

[{% for trainer in object_list %}{% thumbnail trainer.profile_picture "250x250" crop="center" as im %}
    {"im":"{{ im.url }}",
        "meta": {
            "Name": "{{ trainer.first_name }}{{ trainer.last_name }}",
            "pk":"{{ trainer.pk }}",
            "LC: ": "{{trainer.lc}}",
            "Trainings delivered: ":"{{trainer.trainings_delivered}}",
            "Speaks: ": "{{trainer.languages}}",
            "Contact: ":"{{trainer.contact}}",
            "Favourite Trainings: ":"{{trainer.preferred_topics}}"
        }
    },
    {% endthumbnail %}{% endfor %}{"im":"None","meta":{"pk":"None"}}]
