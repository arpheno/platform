{% load thumbnail %}
<h2 class="post_title">Trainers</h2>
<ul>
    {% for trainer in object_list %}
    {% thumbnail trainer.profile_picture "250x250" crop="center" as im %}
    <li class="user-image">
    <img src="{{ im.url }}" width="{{ im.width }}" height="{{ im.height }}">
    <div class="comment">
        <ul>
            <li>{{ trainer.first_name }}{{ trainer.last_name }}</li>
            <li>LC: {{ trainer.lc }}</li>
            <li>Trainings delivered: {{ trainer.trainings_delivered }}</li>
            <li>Speaks {{ trainer.languages }}</li>
            <li>Contact: {{ trainer.contact }}</li>
            <li>Favourite Trainings {{ trainer.preferred_topics }}</li>

        </ul>
    </div>
    </li>
    {% endthumbnail %}
    {% endfor %}
</ul>
