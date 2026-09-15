from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

ROOT = Path(__file__).resolve().parent
out = ROOT / "K9_arxiv_preview.pdf"
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="TitleCenter", parent=styles["Title"], alignment=TA_CENTER, fontSize=17, leading=21, spaceAfter=12))
styles.add(ParagraphStyle(name="Abstract", parent=styles["BodyText"], leftIndent=28, rightIndent=28, fontSize=9.3, leading=12, spaceAfter=13))
styles.add(ParagraphStyle(name="Section", parent=styles["Heading1"], fontSize=13, leading=16, spaceBefore=10, spaceAfter=5))
styles.add(ParagraphStyle(name="Small", parent=styles["BodyText"], fontSize=8.2, leading=10))

def P(s, style="BodyText"):
    return Paragraph(s, styles[style])

story = [
    P("A Computer-Assisted Classification of Knots Realizable with At Most Nine Sticks", "TitleCenter"),
    P("The K9 Computer-Assisted Proof Project<br/>September 2026", "Abstract"),
    P("<b>Abstract.</b> We give a reproducible computer-assisted classification of ordinary unoriented knot types which admit a polygonal realization with at most nine straight edges (sticks), with mirrors identified. Subject to three explicit mathematical inputs - the complete rank-three oriented-matroid catalogue on eight elements, the standard low-crossing knot census, and Calvo's at-most-eight-stick classification - we prove that the set consists of 38 types. Subtracting Calvo's twelve at-most-eight types gives exactly 26 types whose stick number is nine. The proof combines a general-position roof reduction, finite source enumeration, strict diagram certificates, and exact rational-coordinate witnesses.", "Abstract"),
    P("1. Statement and conventions", "Section"),
    P("For a knot type K, let s(K) be the least number of edges in an embedded closed polygon in R^3 representing K, and write K9={K:s(K)<=9}. Knots are ordinary, unoriented types and mirrors are identified. Let S be the 38 types listed below."),
    Table([["class", "types"], ["unknot", "0_1"], ["3-6 crossings", "3_1, 4_1, 5_1, 5_2, 6_1, 6_2, 6_3"], ["7 crossings", "7_1,...,7_7"], ["8 crossings", "8_16, 8_17, 8_18, 8_19, 8_20, 8_21"], ["9 crossings", "9_29, 9_34, 9_35, 9_39,...,9_49"], ["composite", "square, granny, 3_1#4_1"]], colWidths=[1.25*inch, 5.4*inch], style=TableStyle([('GRID',(0,0),(-1,-1),.25,colors.grey),('BACKGROUND',(0,0),(-1,0),colors.lightgrey),('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),('FONTSIZE',(0,0),(-1,-1),8)])), Spacer(1,8),
    P("<b>Theorem.</b> Under the external inputs and certificate checks described here, K9=S."),
    P("Calvo's Theorem 1(iv) gives twelve mirror-folded at-most-eight types: 0_1, 3_1, 4_1, 5_1, 5_2, 6_1, 6_2, 6_3, square, granny, 8_19, 8_20. Hence the exact-nine list is 7_1-7_7; 8_16, 8_17, 8_18, 8_21; 9_29, 9_34, 9_35, 9_39-9_49; and 3_1#4_1, for a total of 26 types."),
    P("2. Proof architecture", "Section"),
    P("The proof is a pair of inclusions. Exact rational-coordinate witnesses establish S subset K9. For the reverse inclusion, a nine-stick polygon is put in general position and reduced to a seven-crossing branch or a finite signed diagram corpus. Every corpus record is normalized under the global back-side operation, traversal reversal, relabelling, and mirror folding, then connected by a replayable certificate DAG to S. The gates are G1 source coverage, G2-G4 normalization and naming, G5 the 38 witnesses, and G6 the low-crossing and Calvo inputs."),
    P("3. Finite source reduction", "Section"),
    P("After subdivision and perturbation, an exposed vertex becomes a roof under F(x,y,z)=(x/z,y/z,1/z); the remaining seven edges carry finite affine heights. Radial projection gives a uniform rank-three oriented matroid on eight elements. The complete external catalogue has 135 classes. The replay enumerates 43,545,600 source contexts, retains 5,269,252 assignments after source-fibre union, and produces 83,023 signed records. Four-line and five-line identities are necessary height conditions. No conjectural global a2 bound is used."),
    P("4. Certificates and complete coverage", "Section"),
    P("The global back-side view exchanges every over/under choice and preserves the ordinary knot type. It yields 52,347 representatives: 1,068 fixed flip orbits, 30,676 paired orbits, and 20,603 one-sided representatives. Strict RI, RII, RIII, and proper-strand-pickup certificates preserve darts, ports, cyclic orders, and parent hashes. The naming DAG has exact domain 83,023 and exact image 52,347; missing, duplicate, foreign, and non-S terminals are zero."),
    P("5. External inputs and limitations", "Section"),
    P("The oriented-matroid catalogue, low-crossing census, standard DT naming database, and Calvo's theorem are external inputs. The offline package contains frozen sources, certificates, exact witnesses, a fixed Windows x64 runtime, and verify.ps1. The relocated replay returned PASS_PORTABLE_FULL_PROOF_CHAIN, with PASS_EXACT_COMPLETE_COVER for the graph stage and PASS_FRESH_EXACT_38_INCLUSIONS for witnesses. This is a computer-assisted theorem under the stated inputs, not a formal verification of the operating system, compiler, Python implementation, or cited classifications, and it does not replace a future purely structural proof."),
    P("References", "Section"),
    P("Calvo, Geometric Knot Spaces and Polygonal Isotopy, arXiv:math/9904037v2, Theorem 1(iv). Finschi, Catalog of Oriented Matroids, uniform rank-three catalogue on eight elements. Menasco, Alternating Knots, arXiv:1901.00582v1.", "Small")]

doc = SimpleDocTemplate(str(out), pagesize=letter, rightMargin=.75*inch, leftMargin=.75*inch, topMargin=.7*inch, bottomMargin=.7*inch, title="K9 Computer-Assisted Classification")
doc.build(story)
print(out)
