<!-- templates/email.html -->
<h1>Contact Us</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <div class="form-actions">
      <button type="submit">Send</button>
    </div>
</form>