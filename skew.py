def skew_label(df, col):
    skew = round(df[col].skew(),2)
    
    if skew < -1 or skew > 1:
        label = 'Highly Skewed'
    elif skew >= -1 and skew <= -.5:
        label = 'Moderately Skewed'
    elif skew <= 1 and skew >= .5:
        label = 'Moderately Skewed'
    else:
        label = 'Approximately Symmetric'
    
    return label