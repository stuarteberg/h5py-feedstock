def jinja_config(jinja_env):
    """
    Augment the given jinja2 environment with additional
    variables/functions specifically for this recipe.
    """
    jinja_env.filters['compatible'] = compatible
    jinja_env.filters['majorminor'] = majorminor

def compatible(version, significant_parts=2):
    """
    Jinja filter.
    
    Examples:
    
        {{ '1.2' | compatible }} --> 1.2*
        {{ '1.2.3' | compatible }} --> 1.2*
        {{ '1.2.3.4' | compatible }} --> 1.2*
    
        {{ '1.2' | compatible(3) }} --> 1.2*
        {{ '1.2.3' | compatible(3) }} --> 1.2.3*
        {{ '1.2.3.4' | compatible(3) }} --> 1.2.3*
    
    """
    return '.'.join( version.split('.')[:significant_parts] ) + '*'

def majorminor(version):
    """
    Shorten version for inclusion in a build string.
    
    Examples:
    
        {{ '2.7.9' | majorminor }} --> 27
        {{ '1.10' | majorminor }} --> 110
    """
    return ''.join( version.split('.')[:2] )

