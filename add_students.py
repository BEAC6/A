#!/usr/bin/env python3
"""
سكريبت إضافة الطلاب الجدد إلى منصة المسابقات الرياضية
Script to add new students to the math competition platform
"""

import os
import sys
import django

# إعداد Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alhassan.settings')
django.setup()

from competitions.models import Participant

def add_students():
    """إضافة الطلاب الجدد"""
    
    # بيانات الطلاب الجدد
    students_data = [
        {
            'name': 'فاطمة الزهراء باعسري',
            'grade': 8,  # المستوى الثاني إعدادي
            'group': 1   # الفوج الأول
        },
        {
            'name': 'عمران بلقاري',
            'grade': 8,  # المستوى الثاني إعدادي
            'group': 1   # الفوج الأول
        }
    ]
    
    print("🎓 بدء إضافة الطلاب الجدد...")
    print("=" * 50)
    
    added_count = 0
    skipped_count = 0
    
    for student_data in students_data:
        name = student_data['name']
        grade = student_data['grade']
        group = student_data['group']
        
        # التحقق من وجود الطالب مسبقاً
        existing_student = Participant.objects.filter(
            name=name,
            grade=grade,
            group=group
        ).first()
        
        if existing_student:
            print(f"⚠️  الطالب {name} موجود بالفعل - تم تخطيه")
            skipped_count += 1
            continue
        
        try:
            # إنشاء الطالب الجديد
            student = Participant.objects.create(
                name=name,
                grade=grade,
                group=group
            )
            
            print(f"✅ تمت إضافة الطالب: {name}")
            print(f"   📚 المستوى: {student.get_grade_display()}")
            print(f"   👥 الفوج: {student.get_group_display()}")
            print(f"   📅 تاريخ الإضافة: {student.created_at.strftime('%Y-%m-%d %H:%M')}")
            print()
            
            added_count += 1
            
        except Exception as e:
            print(f"❌ خطأ في إضافة الطالب {name}: {str(e)}")
            print()
    
    print("=" * 50)
    print("📊 ملخص العملية:")
    print(f"✅ تم إضافة {added_count} طالب/طالبة جديد")
    print(f"⚠️  تم تخطي {skipped_count} طالب/طالبة (موجود مسبقاً)")
    print(f"📈 إجمالي الطلاب في النظام: {Participant.objects.count()}")
    
    return added_count, skipped_count

def list_students_by_grade_and_group():
    """عرض قائمة الطلاب حسب المستوى والفوج"""
    
    print("\n" + "=" * 60)
    print("📋 قائمة الطلاب في المستوى الثاني إعدادي - الفوج الأول")
    print("=" * 60)
    
    # البحث عن طلاب المستوى الثاني إعدادي - الفوج الأول
    students = Participant.objects.filter(
        grade=8,  # المستوى الثاني إعدادي
        group=1   # الفوج الأول
    ).order_by('name')
    
    if students.exists():
        print(f"📊 عدد الطلاب: {students.count()}")
        print()
        
        for i, student in enumerate(students, 1):
            print(f"{i:2d}. {student.name}")
            print(f"    📚 المستوى: {student.get_grade_display()}")
            print(f"    👥 الفوج: {student.get_group_display()}")
            print(f"    📅 تاريخ الإضافة: {student.created_at.strftime('%Y-%m-%d')}")
            print()
    else:
        print("❌ لا يوجد طلاب في هذا المستوى والفوج")
    
    print("=" * 60)

def show_all_grades_summary():
    """عرض ملخص جميع المستويات"""
    
    print("\n" + "=" * 60)
    print("📊 ملخص جميع المستويات الدراسية")
    print("=" * 60)
    
    # الحصول على جميع المستويات المتاحة
    grades = Participant.objects.values_list('grade', flat=True).distinct().order_by('grade')
    
    total_students = 0
    
    for grade in grades:
        grade_students = Participant.objects.filter(grade=grade)
        grade_count = grade_students.count()
        total_students += grade_count
        
        # الحصول على اسم المستوى
        grade_name = dict(Participant.GRADE_CHOICES).get(grade, f"المستوى {grade}")
        
        print(f"📚 {grade_name}: {grade_count} طالب/طالبة")
        
        # عرض توزيع الأفواج
        group1_count = grade_students.filter(group=1).count()
        group2_count = grade_students.filter(group=2).count()
        
        if group1_count > 0:
            print(f"   👥 الفوج الأول: {group1_count}")
        if group2_count > 0:
            print(f"   👥 الفوج الثاني: {group2_count}")
        print()
    
    print(f"📈 إجمالي الطلاب في جميع المستويات: {total_students}")
    print("=" * 60)

def main():
    """الدالة الرئيسية"""
    
    print("🎓 منصة المسابقات الرياضية - إدارة الطلاب")
    print("=" * 60)
    print()
    
    try:
        # إضافة الطلاب الجدد
        added, skipped = add_students()
        
        # عرض قائمة طلاب المستوى الثاني إعدادي - الفوج الأول
        list_students_by_grade_and_group()
        
        # عرض ملخص جميع المستويات
        show_all_grades_summary()
        
        print("\n🎉 تمت العملية بنجاح!")
        
        if added > 0:
            print(f"✅ تم إضافة {added} طالب/طالبة جديد إلى النظام")
            print("🌐 يمكن للطلاب الآن الدخول إلى المنصة والمشاركة في المسابقات")
            print(f"🔗 رابط دخول الطلاب: http://192.168.1.156:8000/student/login/")
            print("🔑 رمز دخول الطلاب: ben25")
        
    except Exception as e:
        print(f"❌ حدث خطأ: {str(e)}")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    if success:
        print("\n✅ تم تنفيذ السكريبت بنجاح")
    else:
        print("\n❌ فشل في تنفيذ السكريبت")
        sys.exit(1)
