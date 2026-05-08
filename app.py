{% extends "base.html" %}
{% set active_page = "reports" %}
{% block title %}Reports{% endblock %}

{% block content %}
<div class="page-header">
  <h1 class="page-title">Reports</h1>
  <p class="page-subtitle">Query outputs (same idea as HeidiSQL result grids) shown in the front end.</p>
</div>

<div style="display:flex; gap:10px; flex-wrap:wrap; margin-top:14px;">
  <a class="btn btn-secondary btn-sm" href="{{ url_for('reports', r='daily_sales') }}">Daily Sales</a>
  <a class="btn btn-secondary btn-sm" href="{{ url_for('reports', r='sales_lines') }}">Sales Lines</a>
  <a class="btn btn-secondary btn-sm" href="{{ url_for('reports', r='low_stock') }}">Low Stock</a>
  <a class="btn btn-secondary btn-sm" href="{{ url_for('reports', r='purchasing_orders') }}">Purchasing Orders</a>
  <a class="btn btn-secondary btn-sm" href="{{ url_for('reports', r='inventory_adjustments') }}">Inventory Adjustments</a>
</div>

<hr class="sep">

<h2 class="section-title">{{ title }}</h2>

<div class="table-wrapper">
  <table>
    <thead>
      <tr>
        {% for c in columns %}
          <th>{{ c }}</th>
        {% endfor %}
      </tr>
    </thead>
    <tbody>
      {% if rows and rows|length > 0 %}
        {% for r in rows %}
          <tr>
            {% for c in columns %}
              <td>{{ r[c] }}</td>
            {% endfor %}
          </tr>
        {% endfor %}
      {% else %}
        <tr>
          <td colspan="{{ columns|length if columns|length else 1 }}" style="text-align:center; opacity:.75;">
            No results.
          </td>
        </tr>
      {% endif %}
    </tbody>
  </table>
</div>

{% endblock %}