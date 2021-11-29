def rerata(*myData):
    #values
    sum=0
    i=0

    #input myData
    for data in myData:
        sum += data
        i += 1

    hasil=sum/i
    print('Rata-ratanya adalah: ',hasil)
