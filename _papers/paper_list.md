---
layout: list
---

{{page.title}}

<ul class="posts">
    {% for post in papers %}
      <li><span>{{ post.date | date_to_string }}</span>
      <a href="https://github.com/haiy/haiy.github.io/edit/master/{{post.path}}" target=_blank> &raquo; </a>
    {% endfor %}
  </ul>
