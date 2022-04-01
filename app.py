from flask import Flask, render_template

app = Flask(__name__)

###################################################################################
# Hlavne #######################################################################


@app.route('/')
@app.route('/blog')
def main_page():  # put application's code here
    return render_template('categories_intro_page_contact.html')


@app.route('/contact_me')
def contact_me():
    return render_template('contact_me.html')


###################################################################################
# kategorie #######################################################################

@app.route('/health_fitness')
def health_fitness():
    return render_template('blog_categories/Health/choose_blog_health.html')


@app.route('/health_fitness/blog_health_1')
def blog_health_1():
    return render_template('specific_blogs/HealthFitness/blog_health_brain.html')


###################################################################################
# specificke blogy #######################################################################





if __name__ == '__main__':
    app.run()
