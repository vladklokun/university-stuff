#include <vcl.h>
#pragma hdrstop

#include "Unit1.h"

#pragma package(smart_init)
#pragma resource "*.dfm"
TForm1 *Form1;

__fastcall TForm1::TForm1(TComponent* Owner) : TForm(Owner)
{
}

int prognum = 0;
void __fastcall TForm1::Button1Click(TObject *Sender)
{
	++prognum;
	UnicodeString strbuf = "Моя программа №" + IntToStr(prognum);
	Label1->Caption = strbuf;
}