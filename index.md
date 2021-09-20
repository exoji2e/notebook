---
layout: base
---

<script>
var clip = function(id) {
    var el = document.getElementById(id);
    var txt = el.textContent.trim()
    navigator.clipboard.writeText(txt);
};
</script>

# Competitive Programming Notebook

A selection of algorithms and data structures used in programming competitions by the team Rainbow Unicode Characters.

[GitHub repo](https://github.com/exoji2e/notebook)


<ul>
{% for part in site.data.code_files %}
    <li><a href="#{{part.name}}">{{part.name}}</a>
    <ul>
    {% for file in part.files %}
        <li><a href="#{{file.name}}">{{file.name}}</a></li>
    {% endfor %}
    </ul>
    </li>
{% endfor %}
</ul>



{% for part in site.data.code_files %}
<a name="{{part.name}}">
## {{ part.name }}

    {% for file in part.files %}
<a name="{{file.name}}">

<h3>{{ file.name }} <span title="Copy" style="cursor:pointer;" class="fa fa-copy" onclick="clip('box-{{file.name}}')" /></h3>

<div id="box-{{file.name}}">
        {% if file.lang == 'java' %}
        {% highlight java %}{% include_relative {{file.path}} %}{% endhighlight %}
        {% elsif file.lang == 'cpp' %}
        {% highlight cpp %}{% include_relative {{file.path}} %}{% endhighlight %}
        {% else %}
        {% highlight python %}{% include_relative {{file.path}} %}{% endhighlight %}
        {% endif %}
</div>
    {% endfor %}
{% endfor %}