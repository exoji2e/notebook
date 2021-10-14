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
<style>
.copy {
    color: #666;
    cursor: pointer;
}
.copy:hover {
    color: #444;
}

</style>

# Competitive Programming Notebook

A selection of algorithms and data structures used in programming competitions by the team Rainbow Unicode Characters.

[GitHub repo](https://github.com/exoji2e/notebook)


<ul>
{% assign cnt = 0 %}
{% for part in site.data.code_files %}
    <li><a href="#{{part.name}}">{{part.name}}</a>
    <ul>
    {% for file in part.files %}
    {% assign cnt = cnt | plus: 1 %}
        <li><a href="#code-{{ cnt }}">{{file.name}}</a></li>
    {% endfor %}
    </ul>
    </li>
{% endfor %}
</ul>



{% assign cnt = 0 %}
{% for part in site.data.code_files %}
<a name="{{part.name}}">
## {{ part.name }}

{% for file in part.files %}
{% assign cnt = cnt | plus: 1 %}
<a name="code-{{ cnt }}">

<h3>{{ file.name }} <span title="Copy" class="fa fa-copy copy" onclick="clip('box-{{ cnt }}')" /></h3>

<div id="box-{{ cnt }}">
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