from pyscript import document


def szamit (event):
    szam1=float(document.queryselector("#szam1").value)
    szam1=float(document.queryselector("#szam2").value)
    muvelet=float(document.queryselector("#muvelet").value)
    document.queryselector("#muvelet").innerText="Tibi"
    
      
def torol(event):
    document.queryselector("#szam1").value=""
    document.queryselector("#szam2").value=""
    document.queryselector("#eredmeny").innerText=""
    document.queryselector("#muvelet").selectedIndex=0
    

