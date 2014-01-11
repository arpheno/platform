{% load thumbnail %}
[{% for trainer in object_list %}{% thumbnail trainer.profile_picture "200x200" crop="center" as im %}
    {
        "pk":"{{ trainer.pk }}",
        "first_name": "{{ trainer.first_name }}",
        "last_name": "{{ trainer.last_name }}",
        "im":"{{ im.url }}",
        "general": {
            "date_of_birth": "{{ trainer.date_of_birth }}"
        },
        "eestec":{
            "lc": "{{ trainer.lc }}",
            "joined_eestec_on": "{{ trainer.joined_eestec_on }}"
        },
        "trt":{
            "trainings_delivered": "{{ trainer.trainings_delivered }}",
            "preferred_topics": "{{ trainer.preferred_topics }}"
        },
        "contact":{
            "mobile": "{{ trainer.mobile }}",
            "facebook": "{{ trainer.facebook }}",
            "hangout": "{{ trainer.hangout }}",
            "skype": "{{ trainer.skype }}"
        }
    },
    {% endthumbnail %}{% endfor %}
    {"pk":"None"}
]
