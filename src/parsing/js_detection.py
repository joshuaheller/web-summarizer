# checks if JavaScript is needed by checking for the noscript tag and the length of the body text.
def check_javascript_needed(body):
    if check_noscript(body):
        return True
    elif len(body.get_text()) <= 2000:
        return True
    else:
        return False
 
# checks for the noscript tag and if it is present, it checks if the text contains certain phrases that indicate the need for JavaScript.
def check_noscript(body):
    noscript_tag = body.find('noscript')
    if noscript_tag:
        body_lc = body.noscript.get_text().lower()
        phrases = ['enable javascript', 'javascript is required', 'javascript is disabled']
        for phrase in phrases:
            if phrase.lower() in body_lc:
                return True
    return False